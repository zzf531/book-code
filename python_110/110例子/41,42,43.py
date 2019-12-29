"""
40,x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串
------------os.path.join()方法，拼接路径
"""
x = ''
x1 = ','
y = '456'
z = ["d", "e", "f"]
n = x1.join(y)
m = x.join(z)
print(n)
print(m)

"""
41、举例说明异常模块中try except else finally的相关意义
try..except..else没有捕获到异常，执行else语句
try..except..finally不管是否捕获到异常，都执行finally语句
"""

try:
    raise IndexError
except IndexError as e:
    print({'错误是'}, e)
else:
    print('我看看有没有异常啊')

try:
    raise IndexError
except IndexError as e:
    print({'错误是'}, e)
finally:
    print('不管有没有异常,我都要执行的')

"""
42、python中交换两个数值
"""
a, b = 3, 4
print(a, b)
a, b = b, a
print(a, b)

print('---------------------43------------')
"""
43、举例说明zip（）函数用法
会以一个或多个序列（可迭代对象）做为参数，
*********返回一个元组的列表。************
同时将这些序列中并排的元素配对。
zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;
当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。
"""
a1 = [1, 2, 3, 4]
b1 = ['a', 'b', 'c']
res = [i for i in zip(a1, b1)]
print(res)
