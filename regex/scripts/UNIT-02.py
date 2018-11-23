#!/usr/bin/python3

'''
RegEx之提取浮点数
'''

import re

numbox = '-0.33|0.66|0.99|2.33'

match1 = '-?[1-9]\d*\.\d+'
match2 = '-?0\.\d*[1-9]\d*'

result = re.findall(match1 + '|' + match2, numbox)

for val in result:
    print(val, end = ' ')
