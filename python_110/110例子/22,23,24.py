"""
22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
set 去重复,然后转成list,利用sort方法排序.reverse = False是从小到大排序
list 的 list.sort() 方法。这个方法会修改原始的 list（返回值为None）。
通常这个方法不如sorted()方便-如果你不需要原始的 list，list.sort()方法效率会稍微高一些。"""
s = 'ajldjlajfdljfddd'
s = set(s)
s = list(s)
s.sort(reverse=False)
# s = s.sort(reverse=False)
res = "".join(s)
print(res)


"""
23.用lambda函数实现两数相乘
"""
sum2 = lambda x, y: x*y
print(sum2(3, 2))


"""
24.字典根据键值对从小到大排序
sort是对应在list上的方法,sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 
方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
-------------------------------------------------
sorted(iterable, key=None, reverse=False)  
iterable -- 可迭代对象
key -- 主要是用来比较的元素,只有一个参数，具体的函数的参数就是取自于可迭代
对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- True 降序, False 升序 (默认) 
"""
dic = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
lis = sorted(dic.items(), key=lambda i: i[0], reverse=False)
print(lis)

print(dict(lis))

print("# 利用key进行倒序排序")
example_list = [5,0,6,1,2,4,5]
result_list = sorted(example_list, key=lambda x: x*-1)
print(result_list)

