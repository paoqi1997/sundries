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
                    printInfo('Get token succ, tag: %s'%sTag)
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
                printInfo('Failed to request v2 api, tag: %s'%sTag)

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
                    printInfo('Failed to request v1 api, tag: %s'%sTag)

if __name__ == '__main__':
    sHelp = '''Usage:
    python3 main.py <tagname(s)>
Examples:
    python3 main.py nginx
    python3 main.py nginx,redis'''
    if len(argv) <= 1:
        print(sHelp)
        exit(1)

    printInfo('Begin.')

    lstTagName = argv[1].split(',')

    oAsyncWorker = AsyncWorker()
    oAsyncWorker.run(lstTagName)

    printInfo('End.')
