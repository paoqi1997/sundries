#!/usr/bin/python3

import json
import os
import time
from sys import argv, path

import requests

def sTime():
    fTime = time.time()
    group = time.localtime(fTime)
    return time.strftime('%Y-%m-%d %H:%M:%S', group)

def printInfo(sInfo):
    print('%s: %s'%(sTime(), sInfo))

def writeToFile(sFileName, lstTag):
    with open(os.path.join(path[0], sFileName), 'w') as oFile:
        oFile.writelines('\n'.join(lstTag))

if __name__ == '__main__':
    if len(argv) <= 1:
        print('Usage: python3 main.py <name>')
        exit(1)

    printInfo('Begin.')

    sName = argv[1]
    oSession = requests.Session()

    # get token
    dParams = {
        'service': 'registry.docker.io',
        'scope': 'repository:library/%s:pull'%sName
    }
    oRep = oSession.get(url='https://auth.docker.io/token', params=dParams)

    dResult = oRep.json()
    sToken = dResult['token']

    printInfo('Get token.')

    # request v2 api
    dHeaders = {
        'Authorization': 'Bearer %s'%sToken
    }
    oRep = oSession.get(
        url='https://registry.hub.docker.com/v2/library/%s/tags/list'%sName, headers=dHeaders
    )

    sFileName = ('%s.tags'%sName).replace('/', '.')

    if oRep.status_code == 200:
        printInfo('Request v2 api succ.')
        dResult = oRep.json()
        lstTag = dResult['tags']
        writeToFile(sFileName, lstTag)
    else:
        # request v1 api
        oRep = oSession.get(url='https://registry.hub.docker.com/v1/repositories/%s/tags'%sName)
        if oRep.status_code == 200:
            printInfo('Request v1 api succ.')
            sResult = '{\"result\": %s}'%oRep.text
            dResult = json.loads(sResult)
            lstTag = [dElement['name'] for dElement in dResult['result']]
            writeToFile(sFileName, lstTag)
        else:
            printInfo('None.')
