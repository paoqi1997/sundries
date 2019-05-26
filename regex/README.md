# 简述

面向Regular Expression的基本教程。

# 说明

Python大法好！目前我的版本为3.6.5，我将使用它来讲解以下正则表达式。

# 正文

首先导入相关的包。

```python
import re
```

## 1. 匹配日期

如果你想匹配'YYYY-MM-DD'这样的日期格式，可以这么做：

```python
string = 'Start Time: 1970-01-01'
result = re.search('([0-9]{4})-([0-9]{2})-([0-9]{2})', string)
# Output: 1970-01-01
print(result.group())
```

实际上，日期是有着严格的格式限制的，首先我们匹配平年：

```python
string = 'School Time: 2015-09-01'
match1 = '[0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3}'
match2 = '(0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01])'
match3 = '(0[469]|11)-(0[1-9]|[12][0-9]|30)'
match4 = '02-(0[1-9]|1[0-9]|2[0-8])'
xmatch = '(' + match1 + ')' + '-' +
         '(' +
         '(' + match2 + ')' + '|' +
         '(' + match3 + ')' + '|' + '(' + match4 + ')' + ')'
result = re.search(xmatch, string)
# Output: 2015-09-01
print(result.group())
```

接下来要匹配的是闰年，关键是要处理好2月29日这种特殊情况：

```python
string = 'Target Time: 2008-02-29'
match5 = '[0-9]{2}(0[48]|[2468][048]|[13579][26])'
match6 = '(0[48]|[2468][048]|[13579][26])00'
match7 = '02-29'
ymatch = '(' + match5 + '|' + match6 + ')' + '-' + match7
result = re.search(ymatch, string)
# Output: 2008-02-29
print(result.group())
```

接上文，将平年与闰年的正则表达式合并后就是我们想要的正则表达式：

```python
zmatch = '(' + xmatch + ')' + '|' + '(' + ymatch + ')'
```

## 2. 匹配时间

相比日期，时间的匹配规则要简单得多。在这里我们采用的是24小时制：

```python
string = 'Current Time: 20:30:00'
match1 = '[01][0-9]|2[0-3]'
match2 = '[0-5][0-9]'
match3 = '[0-5][0-9]'
result = re.search('(' + match1 + ')' + ':' +
                   '(' + match2 + ')' + ':' + '(' + match3 + ')', string)
# Output: 20:30:00
print(result.group())
```

## 3. 后续

后续操作就交给Python脚本吧！

```python
exit()
```
