#!/usr/bin/python3

'''JSON Object & Array'''

import json
import os
import sys

dData = {
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

sFileName = os.path.join(sys.path[0], 'data.json')

# json.dumps: dict -> str
sData = json.dumps(dData)
print(sData)

# json.loads: str -> dict
dData = json.loads(sData)
print(dData)

# json.dump: dict -> data.json
with open(sFileName, 'w') as oFile:
    json.dump(dData, oFile)

# json.load: data.json -> dict
with open(sFileName, 'r') as oFile:
    dData = json.load(oFile)
    print(dData)
