# -*- coding:utf-8 -*-

import re

""" 
则以匹配
利用python原生的面向对象特性，忽略保存中间过程产生结果，
如果匹配失败，会抛出AttributeError
"""
bt = 'bat|bet|bit'
print('匹配结果：', re.match(bt, 'bat').group())

m1 = re.match(bt, 'He bit me!')  # 不能匹配字符串
if m1 is not None:
    print(m1.group())

m2 = re.search(bt, 'He bit me!')  # 通过搜索查询 'bit'
if m2 is not None:
    print(m2.group())
print("**匹配任何单个字符开始" * 8)


anyend = '.end'
a = re.match(anyend, 'bend')
if a is not None:
    print(a.group())

a2 = re.match(anyend, 'end')  # 不匹配非字符
if a2 is not None:
    print('a2的值', a2.group())

a3 = re.match(anyend, '\nend')  # 除了\n 之外的任何字符串
if a3 is not None:
    print('a3的值', a3.group())

a4 = re.search(anyend, 'The end.')
if a4 is not None:
    print('a4的值', a4.group())



