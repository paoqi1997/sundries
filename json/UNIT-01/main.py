#!/usr/bin/python3

'''
JSON对象
'''

import json
import platform
import sys

dic = {
    'name': 'paoqi',
    'age': 22,
    'extra': {
        'country': 'China',
        'province': 'Guangdong',
        'city': 'Shenzhen'
    }
}

if platform.system() is 'Windows':
    jsonfile = sys.path[0] + '\\' + 'data.json'
else:
    jsonfile = sys.path[0] + '/' + 'data.json'

# Python Object -> JSON(String)
jsondata = json.dumps(dic)
print(jsondata)

with open(jsonfile, 'r') as f:
    # JSON(File) -> Python Object
    pydata = json.load(f)

# name: paoqi
# age: 22
# extra.country: China
# extra.province: Guangdong
# extra.city: Shenzhen
print('name:', pydata['name'])
print('age:', pydata['age'])
print('extra.country:', pydata['extra']['country'])
print('extra.province:', pydata['extra']['province'])
print('extra.city:', pydata['extra']['city'])
