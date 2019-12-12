"""
12、简述with方法打开处理文件帮我我们做了什么？
打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open
写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况
，都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close
（当然还有其他自定义功能，有兴趣可以研究with方法源码）
"""


"""
13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，
并使用列表推导式提取出大于10的数，最终输出[16,25]
"""
litss =[1, 2, 3, 4, 5]


def fn(x):
    return x ** 2

res = map(fn, litss)
res2 = map(lambda x: x**2, litss)  # 匿名函数

res3 = [i for i in res if i  > 10]
print(res3)

print('--------------14题解答')
"""
14、python中生成随机整数、随机小数、0--1之间小数方法
随机整数：random.randint(a,b),生成区间内的整数
随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
0-1随机小数：random.random(),括号中不传参
"""
import random

result = random.randint(10,20)
res123 = random.random()
print(result)
print(res123)


"""
15、避免转义给字符串加哪个字母表示原始字符串？ 
（\n 换行 \r 回车 \b 退格， \(在行尾时) 续行符）
r , 表示需要原始字符串，不转义特殊字符
"""
