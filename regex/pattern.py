def getDatePattern():
    sPattern = '([0-9]{4})-([0-9]{2})-([0-9]{2})'
    return sPattern

def getDatePattern_v2():
    ### 不考虑02-29
    # 合法年份
    sPattern1 = '[0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3}'
    # 合法大月
    sPattern2 = '(0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01])'
    # 合法小月
    sPattern3 = '(0[469]|11)-(0[1-9]|[12][0-9]|30)'
    # 02.01 - 02.28
    sPattern4 = '02-(0[1-9]|1[0-9]|2[0-8])'
    ### 考虑02-29
    # 闰年 - 能被4整除但不能被100整除
    sPattern5 = '[0-9]{2}(0[48]|[2468][048]|[13579][26])'
    # 闰年 - 能被400整除
    sPattern6 = '(0[48]|[2468][048]|[13579][26])00'
    # 02.29
    sPattern7 = '02-29'
    ### 合并
    sPattern_not_0229 = '({p1})-({p2}|{p3}|{p4})'.format(
        p1=sPattern1, p2=sPattern2, p3=sPattern3, p4=sPattern4
    )
    sPattern_0229 = '({p5}|{p6})-{p7}'.format(
        p5=sPattern5, p6=sPattern6, p7=sPattern7
    )
    sPattern = '{p1}|{p2}'.format(p1=sPattern_not_0229, p2=sPattern_0229)
    return sPattern

def getClockPattern():
    sPattern1 = '[01][0-9]|2[0-3]'
    sPattern2 = '[0-5][0-9]'
    sPattern = '({p1}):{p2}:{p2}'.format(p1=sPattern1, p2=sPattern2)
    return sPattern

def getIntPattern():
    sPattern = '-?[1-9]\d*'
    return sPattern

def getFloatPattern():
    sPattern1 = '-?[1-9]\d*\.\d+'
    sPattern2 = '-?0\.\d*[1-9]\d*'
    sPattern = '{p1}|{p2}'.format(p1=sPattern1, p2=sPattern2)
    return sPattern
