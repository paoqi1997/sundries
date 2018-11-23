#!/usr/bin/python3

'''
RegEx之提取整数
'''

import re

lengths = '-50m|100m|200m|400m'

result = re.findall('-?[1-9]\d*', lengths)

for val in result:
    print(val, end = ' ')
