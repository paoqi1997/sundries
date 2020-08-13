#!/usr/bin/python3

import asyncio
import json
import os
import time
from sys import argv, path

import aiohttp
import requests

def sTime():
    fTime = time.time()
    group = time.localtime(fTime)
    return time.strftime('%Y-%m-%d %H:%M:%S', group)

def printInfo(sInfo):
    print('%s: %s'%(sTime(), sInfo))

def writeToFile(sTag, lstTag):
    sFileName = ('%s.tags'%sTag).replace('/', '.')
    with open(os.path.join(path[0], sFileName), 'w') as oFile:
        oFile.writelines('\n'.join(lstTag))

class SyncWorker:
    def __init__(self):
        self.m_oSession = requests.Session()
        self.m_Timeout = 10

    def run(self, lstTag):
        for sTag in lstTag:
            self.pullTag(sTag)

    def getToken(self, sTag):
        dParams = {
            'service': 'registry.docker.io',
            'scope': 'repository:library/%s:pull'%sTag
        }
        oRep = self.m_oSession.get(
            url='https://auth.docker.io/token', params=dParams, timeout=self.m_Timeout
        )
        dResult = oRep.json()
        sToken = dResult['token']
        printInfo('Get token.')
        return sToken

    def pullTag(self, sTag):
        sToken = self.getToken(sTag)
        # request v2 api
        dHeaders = {
            'Authorization': 'Bearer %s'%sToken
        }
        try:
            oRep = self.m_oSession.get(
                url='https://registry.hub.docker.com/v2/library/%s/tags/list'%sTag,
                headers=dHeaders, timeout=self.m_Timeout
            )
        except Exception:
            printInfo('Request v2 api failed, tag: %s'%sTag)
            return

        if oRep.status_code == 200:
            printInfo('Request v2 api succ, tag: %s'%sTag)
            dResult = oRep.json()
            lstTag = dResult['tags']
            writeToFile(sTag, lstTag)
        else:
            # request v1 api
            oRep = self.m_oSession.get(
                url='https://registry.hub.docker.com/v1/repositories/%s/tags'%sTag, timeout=self.m_Timeout
            )
            if oRep.status_code == 200:
                printInfo('Request v1 api succ, tag: %s'%sTag)
                sResult = '{\"result\": %s}'%oRep.text
                dResult = json.loads(sResult)
                lstTag = [dElement['name'] for dElement in dResult['result']]
                writeToFile(sTag, lstTag)
            else:
                printInfo('None.')

class AsyncWorker:
    def __init__(self):
        self.m_Looper = asyncio.get_event_loop()
        self.m_Tasks = []
        self.m_Timeout = aiohttp.ClientTimeout(total=10)

    def __del__(self):
        self.m_Looper.close()

    def run(self, lstTag):
        for sTag in lstTag:
            self.m_Tasks.append(self.pullTag(sTag))
        self.m_Looper.run_until_complete(
            asyncio.wait(self.m_Tasks)
        )

    async def getToken(self, sTag):
        dParams = {
            'service': 'registry.docker.io',
            'scope': 'repository:library/%s:pull'%sTag
        }
        async with aiohttp.ClientSession(timeout=self.m_Timeout) as oSession:
            try:
                async with oSession.get(
                    url='https://auth.docker.io/token', params=dParams
                ) as oRep:
                    dResult = await oRep.json()
                    sToken = dResult['token']
                    printInfo('Get token.')
                    return sToken
            except asyncio.TimeoutError:
                printInfo('Failed to get token, tag: %s'%sTag)
                return ""

    async def pullTag(self, sTag):
        sToken = await self.getToken(sTag)
        if sToken == "":
            return
        dHeaders = {
            'Authorization': 'Bearer %s'%sToken
        }
        async with aiohttp.ClientSession(timeout=self.m_Timeout) as oSession:
            try:
                async with oSession.get(
                    url='https://registry.hub.docker.com/v2/library/%s/tags/list'%sTag, headers=dHeaders
                ) as oRep:
                    if oRep.status == 200:
                        printInfo('Request v2 api succ, tag: %s'%sTag)
                        dResult = await oRep.json()
                        lstTag = dResult['tags']
                        writeToFile(sTag, lstTag)
                    else:
                        await self.reqV1API(sTag)
            except asyncio.TimeoutError:
                printInfo('Request v2 api failed, tag: %s'%sTag)

    async def reqV1API(self, sTag):
        async with aiohttp.ClientSession(timeout=self.m_Timeout) as oSession:
            async with oSession.get(
                url='https://registry.hub.docker.com/v1/repositories/%s/tags'%sTag
            ) as oRep:
                if oRep.status == 200:
                    printInfo('Request v1 api succ, tag: %s'%sTag)
                    sText = await oRep.text()
                    sResult = '{\"result\": %s}'%sText
                    dResult = json.loads(sResult)
                    lstTag = [dElement['name'] for dElement in dResult['result']]
                    writeToFile(sTag, lstTag)
                else:
                    printInfo('None.')

if __name__ == '__main__':
    print(argv)
    if len(argv) <= 2:
        print('Usage: python3 main.py <useAsync> <name>')
        exit(1)

    printInfo('Begin.')

    bAsyncFlag = bool(int(argv[1]))
    lstTagName = argv[2].split(',')

    if bAsyncFlag:
        oAsyncWorker = AsyncWorker()
        oAsyncWorker.run(lstTagName)
    else:
        oSyncWorker = SyncWorker()
        oSyncWorker.run(lstTagName)

    printInfo('End.')
