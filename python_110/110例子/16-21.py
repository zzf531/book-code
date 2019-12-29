"""
16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”）
其中class的类名是不确定的
"""
import re
str = '<div class="nam">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>', str)
print(res)

"""
17、pythonzh中断言方法举例
assert()， 方法，断言成功，程序继续执行，断言失败，则程序报错
"""
a = 3
assert(a > 1)
print("断言成功，程序继续向下执行")

b = 4
# assert(b > 7)
print("断言失败，程序报错")


"""
18、数据表student有id,name,score,city字段，其中name中的名字可有
重复，需要消除重复行,请写sql语句
select distinct name from student
"""


"""
19、10个Linux常用命令
ls  pwd  cd  touch  rm  mkdir  tree  cp  mv  cat  more  grep  echo 
"""


"""
20.python2 和python3区别？ 列举五个
1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存
3、python2中使用ascii编码，python中使用utf-8编码
4、python2中unicode表示字符串序列，str表示字节序列
   python3中str表示字符串序列，byte表示字节序列
5、python2中为正常显示中文，引入coding声明，python3中不需要
6、python2中是raw_input()函数，python3中是input()函数   
"""

"""
21、列出python中可变数据类型和不可变数据类型，并简述原理
不可变数据类型:数值型, 字符串型string, 元组tuple

不允许变量的值发生改变,如果改变了变量的值,相当于新建了一个对象,
对于 相同的值的对象,在内存中则只有一个对象(一个地址)
-------------------------
可变数据类型：列表list和字典dict；

允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，
只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，
不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自
己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实
在在的对象。
"""
print("--------22提测试-----------")
a3 = 3
b3 = 3
print(id(a3), id(b3))  # 不可变,地址相同

a4 = [1,2]
a6 = [1,2]
print(id(a4), id(a6))