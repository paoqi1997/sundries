#!/usr/bin/python3

'''JSON Object & Array'''

import json
import platform
import sys

oDict = {
    'solution': 'db',
    'type': {
        'relational': [{
            'name': 'mysql', 'version': '8.0.19'
        }, {
            'name': 'mariadb', 'version': '10.3.22'
        }],
        'kv': [{
            'name': 'redis', 'version': '5.0.7'
        }]
    }
}

if platform.system() is 'Windows':
    sFileName = '{dir}\\data.json'.format(dir=sys.path[0])
else:
    sFileName = '{dir}/data.json'.format(dir=sys.path[0])

# json.dumps: Dict -> JSON String
sJsonData = json.dumps(oDict)
print(sJsonData)

# json.loads: JSON String -> Dict
oResDict = json.loads(sJsonData)
print(oResDict)

# json.dump: Dict -> JSON File
with open(sFileName, 'w') as oFile:
    json.dump(oDict, oFile)

# json.load: JSON File -> Dict
with open(sFileName, 'r') as oFile:
    oResDict = json.load(oFile)
    print(oResDict)
