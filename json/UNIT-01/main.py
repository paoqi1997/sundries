#!/usr/bin/python3

'''
JSON对象
'''

import json

dic = {
    'name': 'paoqi',
    'age': 18,
    'extra': {
        'country': 'China',
        'province': 'Guangdong',
        'city': 'Shenzhen'
    }
}

# Python Object -> JSON(String)
jsondata = json.dumps(dic)
print(jsondata)

with open('data.json', 'r') as f:
    # JSON(File) -> Python Object
    pydata = json.load(f)

# name: paoqi
# age: 18
# extra.country: China
# extra.province: Guangdong
# extra.city: Shenzhen
print('name:', pydata['name'])
print('age:', pydata['age'])
print('extra.country:', pydata['extra']['country'])
print('extra.province:', pydata['extra']['province'])
print('extra.city:', pydata['extra']['city'])
