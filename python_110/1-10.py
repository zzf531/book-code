# 1.一行代码实现1-100的和
print(sum(range(1, 101)))
print('第一题')
# 2.函数内部修改全局变量
a = 5
def add():
    global a
    a = 3
    print(a)
add()
print(a)
print('第二题')


# 4.字典如何删除键和合并两个字典print(a)
dic = {
    'name': 'zs',
    'age': 18
}
del dic['name']
print(dic)
dic2 = {'sex': 12}
dic.update(dic2)
print(dic)
print('第四题')

"""
5、谈下python的GIL
GIL 是python的全局解释器锁，同一进程中假如有多个线程
运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。
如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，
线程的运行仍是有先后顺序的，并不是同时进行。
多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，
所以多进程可以实现多个进程的同时运行，进程系统资源开销大
"""

# 6.pyton实现列表去重
lsit = [11, 12, 13, 12, 15, 16, 13]
a = set(lsit)

print([x for x in a])
print('第六题')

# fun(*args, **kwargs)中的意识
"""
预先并不知道，函数使用者会传递多少个参数给你，这个场景下使用这两个关键字，
前面的*号才是关键，*args是用来发送一个非键值对的可变参数的参数列表给一个函数
**kwargs 允许你将不定长度的键值对，作为参数传递给一个函数
"""

def demo(a, *args, **kwargs):
    print(a, *args, **kwargs)

demo(123, 456, 579, {'name': 'zzf', 'height': 173.8})
print('第七题')

# 8.Python2 和Python3 range(100)的区别
"""
python2 返回列表， python3返回迭代器节约内存
[1,2,3,4]         range(1,4)
"""

'''
9、一句话解释什么样的语言能够用装饰器
函数可以做为参数传递的语言，可以使用装饰器
'''

'''
10. 简述Python数据类型
1,Booleans［布尔型］ 或为 True［真］ 或为 False［假］。
2,Numbers［数值型］ 可以是 Integers［整数］（1 和 2）、
    Floats［浮点数］（1.1 和 1.2）、Fractions［分数］（ 1/2 和 2/3）；
    甚至是 Complex Number［复数］。
3,Strings［字符串型］ 是 Unicode 字符序列，例如： 一份 html 文档。
4,Bytes［字节］ 和 Byte Arrays［字节数组］， 例如: 一份 jpeg 图像文件。
5,Lists［列表］ 是值的有序序列。
6,Tuples［元组］ 是有序而不可变的值序列。
7,Sets［集合］ 是装满无序值的包裹。
8,Dictionaries［字典］ 是键值对的无序包裹。
'''