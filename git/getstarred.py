from sys import argv, path

import json
import os
import platform

if __name__ == '__main__':
    if len(argv) <= 1:
        sUserName = 'paoqi1997'
    else:
        sUserName = argv[1]

    dParam = {
        'sort': 'created',
        'direction': 'desc',
        'per_page': 30,
        'page': 1
    }

    lstParam = [f'{sKey}={dParam[sKey]}' for sKey in dParam]

    sParams = '&'.join(lstParam)

    # https://docs.github.com/cn/rest/reference/activity#list-repositories-starred-by-a-user
    sUrl = f'"https://api.github.com/users/{sUserName}/starred?{sParams}"'

    lstOption = [
        '-s',
        '-H',
        '"Accept: application/vnd.github.v3+json"'
    ]

    # https://curl.se/mail/lib-2016-03/0202.html
    if platform.system() == 'Windows':
        lstOption.append('--ssl-no-revoke')

    sOptions = ' '.join(lstOption)

    sCmd = f'curl {sOptions} {sUrl}'
    print(sCmd)

    with os.popen(sCmd) as oPipe:
        sResult = oPipe.buffer.read().decode('utf-8')
        lstRepo = json.loads(sResult)

        dOutput = { 'repos': lstRepo }
        sOutput = json.dumps(dOutput, indent=2)

        sFileName = f'{sUserName}.starred.json'
        sFilePath = os.path.join(path[0], sFileName)

        with open(sFilePath, 'w') as oFile:
            oFile.write(f'{sOutput}\n')
