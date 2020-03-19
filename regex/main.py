#!/usr/bin/python3

'''Regular Expression'''

import re
from pattern import *

def groupText(sPattern, sText):
    result = re.search(sPattern, sText)
    return result.group()

def findAllText(sPattern, sText):
    results = re.findall(sPattern, sText)
    return results

if __name__ == '__main__':
    sText = 'Text: 1970-01-01'
    print(groupText(getDatePattern(), sText))

    sText = 'Text: 2015-02-28'
    print(groupText(getDatePattern_v2(), sText))

    sText = 'Text: 2008-02-29'
    print(groupText(getDatePattern_v2(), sText))

    sText = 'Text: 00:30:00'
    print(groupText(getClockPattern(), sText))

    sText = 'Text: -50m|100m|200m|400m'
    for result in findAllText(getIntPattern(), sText):
        print(result, end=' ')
    print()

    sText = 'Text: -0.33|0.66|0.99|2.33'
    for result in findAllText(getFloatPattern(), sText):
        print(result, end=' ')
