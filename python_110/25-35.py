"""
25、利用collections库的Counter方法统计字符串每个单词出现的次数
"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
"""
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

"""
26、字符串a = "not 404 found 张三 99 深圳"，每个词中间
是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
"""


"""
27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素
组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素
作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元
素放到新列表
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newa = filter(lambda x: x%2==1, a)
print(newa)
print([i for i in newa])


"""
28.列表推导式,列表所有奇数并构造新列表 
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res3 = [i for i in a if i % 2 == 1]
print(res3)


"""
29、正则re.complie作用
re.compile是将正则表达式编译成一个对象，加快速度，并重复使用
"""

'''
30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
'''
print(
    type((1,)),
    type((1)),
    type(('1'))
)

"""
31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
"""
list1 = [1, 5, 7, 9]
list2 = [2, 2, 6, 8]
list1.extend(list2)
list1.sort()
print(list1)


"""
32、用python删除文件和用linux命令删除文件方法
python：os.remove(文件名)
linux:       rm  文件名
"""

"""
33、log日志中，我们需要用时间戳记录error,warning等的发生时间，
请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
"""
import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+ ' 星期: ' + str(datetime.datetime.now().isoweekday())
print(a)

"""
34、数据库优化查询方法
外键、索引、联合查询、选择特定字段等等
"""

"""
35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
pychart、matplotlib
"""


"""
36.写一段自定义异常代码
 自定义异常常用raise抛出异常
"""
def fn():
    try:
        for i in range(5):
            if i > 2:
                raise Exception("数字大于2")
    except Exception as ret:
        print(ret)

fn()


'''
37、正则表达式匹配中，（.*）和（.*?）匹配区别？
（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
'''
s = "<a>哈哈</a><a>呵呵</a>"
import re
res5 = re.findall("<a>(.*)</a>", s)
print(res5)
res51 = re.findall("<a>(.*?)</a>", s)
print(res51)


"""
39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
列表推导式的骚操作运行过程：for i in a ,每个i是【1,2】，【3,4】，【5,6】，
for j in i，每个j就是1,2,3,4,5,6,合并后就是结果
"""
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
print(x)