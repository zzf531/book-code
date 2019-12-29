"""
45,写5条常用sql语句
show databases;
show tables;
select * from 表明;
delete from 表名 where id=5;
update students set gender=0,hometown="北京" where id=5
"""

'''
46、a="hello"和b="你好"编码成bytes类型
'''
a = b'hello'
b = "你好".encode()
print(type(a))

"""
48、提高python运行效率的方法
1.使用生成器,以为可以节约内存
2.循环代码优化,避免过多复杂代码执行(Python工匠,第二章有介绍)
3.核心模块用Cython, PyPy等,提高效率
4.多线程,多进程, 协程
5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，
这样可以减少程序判断的次数，提高效率
"""


"""
51、正则匹配，匹配日期2018-03-20

"""
import re
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
res = re.findall(r'dateRange=(.*?)%7C(.*?)&', url)
print(res)