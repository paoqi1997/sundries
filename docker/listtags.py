#!/usr/bin/python3

from sys import argv, path

import asyncio
import json
import os
import time

import aiohttp

def sTime():
    oTimeStruct = time.localtime()
    return time.strftime('%Y-%m-%d %H:%M:%S', oTimeStruct)

def printInfo(sInfo):
    print('[%s] %s'%(sTime(), sInfo))

def writeToFile(sImage, lstTag):
    sDir = os.path.join(path[0], 'tags')
    if not os.path.exists(sDir):
        os.mkdir(sDir)

    sFileName = ('%s.tags'%sImage).replace('/', '.')
    sFilePath = os.path.join(sDir, sFileName)

    with open(sFilePath, 'w') as oFile:
        sTags = '\n'.join(lstTag)
        oFile.write(f'{sTags}\n')

class AsyncWorker:
    def __init__(self):
        self.m_Looper = asyncio.get_event_loop()
        self.m_Tasks = []
        self.m_Timeout = aiohttp.ClientTimeout(total=10)

    def __del__(self):
        self.m_Looper.close()

    def run(self, lstImage):
        for sImage in lstImage:
            self.m_Tasks.append(self.pullTags(sImage))
        self.m_Looper.run_until_complete(asyncio.wait(self.m_Tasks))

    async def getToken(self, sImage):
        dParams = {
            'service': 'registry.docker.io',
            'scope': 'repository:library/%s:pull'%sImage
        }
        async with aiohttp.ClientSession(timeout=self.m_Timeout) as oSession:
            try:
                async with oSession.get(
                    url='https://auth.docker.io/token', params=dParams
                ) as oResp:
                    dResult = await oResp.json()
                    sToken = dResult['token']
                    printInfo('Get token succ, image: %s'%sImage)
                    return sToken
            except asyncio.TimeoutError:
                printInfo('Failed to get token, image: %s'%sImage)
                return ''

    async def pullTags(self, sImage):
        sToken = await self.getToken(sImage)
        if sToken == '':
            return
        dHeaders = {
            'Authorization': 'Bearer %s'%sToken
        }
        async with aiohttp.ClientSession(timeout=self.m_Timeout) as oSession:
            try:
                async with oSession.get(
                    url='https://registry.hub.docker.com/v2/library/%s/tags/list'%sImage, headers=dHeaders
                ) as oResp:
                    if oResp.status == 200:
                        printInfo('Request v2 api succ, image: %s'%sImage)
                        dResult = await oResp.json()
                        lstTag = dResult['tags']
                        writeToFile(sImage, lstTag)
                    else:
                        await self.reqV1API(sImage)
            except asyncio.TimeoutError:
                printInfo('Failed to request v2 api, image: %s'%sImage)

    async def reqV1API(self, sImage):
        async with aiohttp.ClientSession(timeout=self.m_Timeout) as oSession:
            async with oSession.get(
                url='https://registry.hub.docker.com/v1/repositories/%s/tags'%sImage
            ) as oResp:
                if oResp.status == 200:
                    printInfo('Request v1 api succ, image: %s'%sImage)
                    sText = await oResp.text()
                    sResult = '{\"result\": %s}'%sText
                    dResult = json.loads(sResult)
                    lstTag = [dElement['name'] for dElement in dResult['result']]
                    writeToFile(sImage, lstTag)
                else:
                    printInfo('Failed to request v1 api, image: %s'%sImage)

if __name__ == '__main__':
    sHelp = '''Usage:
    python3 listtags.py <image(s)>
Examples:
    python3 listtags.py nginx
    python3 listtags.py nginx,redis'''
    if len(argv) <= 1:
        print(sHelp)
        exit(1)

    printInfo('Begin.')

    lstImage = argv[1].split(',')

    oAsyncWorker = AsyncWorker()
    oAsyncWorker.run(lstImage)

    printInfo('End.')
