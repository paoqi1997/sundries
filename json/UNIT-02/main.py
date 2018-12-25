#!/usr/bin/python3

'''
JSON数组
'''

import json
import platform
import sys

dic = {
    'name': 'xiaoting',
    'age': 20,
    'extra': {
        'cup': 'C',
        'tag': {
            'Teochew': [ 'Chaozhou', 'Jieyang', 'Shantou' ]
        },
        'Internet': [
            {
                'name': 'alibaba', 'business': [ 'taobao', 'tmall' ]
            },
            {
                'name': 'tencent', 'business': [ 'qq', 'wechat' ]
            }
        ]
    }
}

osname = platform.system()
if osname is 'Windows':
    jsonfile = sys.path[0] + '\\' + 'data.json'
elif osname is 'Linux':
    jsonfile = sys.path[0] + '/' + 'data.json'

# Python Object -> JSON(String)
jsondata = json.dumps(dic)
print(jsondata)

with open(jsonfile, 'r') as f:
    # JSON(File) -> Python Object
    pydata = json.load(f)

# name: xiaoting
# age: 20
print('name:', pydata['name'])
print('age:', pydata['age'])

_extra = pydata['extra']

# extra.cup: C
print('extra.cup:', _extra['cup'])

# extra.tag.Teochew: Chaozhou Jieyang Shantou
print('extra.tag.Teochew:', end = ' ')
for ele in _extra['tag']['Teochew']:
    print(ele, end = ' ')
print(end = '\n')

# extra.Internet.1.name: alibaba
# extra.Internet.1.business: taobao tmall
# extra.Internet.2.name: tencent
# extra.Internet.2.business: qq wechat
for i, ele in enumerate(_extra['Internet']):
    print('extra.Internet.{index}.name:'.format(index = i + 1), end = ' ')
    print(ele['name'])
    print('extra.Internet.{index}.business:'.format(index = i + 1), end = ' ')
    for val in ele['business']:
        print(val, end = ' ')
    print(end = '\n')
