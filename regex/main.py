#!/usr/bin/python3

'''Regular Expression'''

import re
from pattern import *

def groupText(sPattern, sText):
    oMatch = re.search(sPattern, sText)
    return oMatch.group()

def findAllText(sPattern, sText):
    lstResult = re.findall(sPattern, sText)
    return lstResult

if __name__ == '__main__':
    # 匹配日期
    sText = 'Text: 1970-01-01'
    print(groupText(getDatePattern(), sText))

    # 匹配日期_v2
    sText = 'Text: 2015-09-01'
    print(groupText(getDatePattern_v2(), sText))
    sText = 'Text: 2008-02-29'
    print(groupText(getDatePattern_v2(), sText))

    # 匹配时间
    sText = 'Text: 00:30:00'
    print(groupText(getClockPattern(), sText))

    # 匹配整数
    sText = 'Text: -50m|100m|200m|400m'
    for sResult in findAllText(getIntPattern(), sText):
        print(sResult, end=' ')
    print()

    # 匹配浮点数
    sText = 'Text: -0.33|0.66|0.99|2.33'
    for sResult in findAllText(getFloatPattern(), sText):
        print(sResult, end=' ')
    print()

    # 匹配从最左边开始一对花括号内的内容
    sText = '{What do you mean{BOOST}?{}} {Emmm...}'
    print(groupText(getBracePattern(), sText))

    # 匹配 IPv4 地址
    sText = '192.168.74.128'
    print(groupText(getIPv4Pattern(), sText))

    # 匹配中文字符
    sText = '你好，我是paoqi'
    print(findAllText(getChinesePattern(), sText))

    # 匹配版本号
    sText = 'nginx-1.18.0'
    print(groupText(getVersionPattern(), sText))
