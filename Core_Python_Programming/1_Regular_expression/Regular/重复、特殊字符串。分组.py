# -*- coding-utf-8 -*-
"""
* 匹配前面正则表达式0次或多次
+ 匹配1次或多次
？匹配0次或1次
"""
import re

patt = '\w+@(\w+\.)?\w+\.com'
a = re.match(patt, 'nobody@xxx.com')
if a is not None:
    print(a.group())

a2 = re.match(patt, 'nobody@xxx.www.com')
if a2 is not None:
    print(a2.group())
