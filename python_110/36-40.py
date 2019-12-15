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


"""
40、x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致，有没有突然感觉字符串的常见操作都不会玩了

顺便建议大家学下os.path.join()方法，拼接路径经常用到，也用到了join,
和字符串操作中的join有什么区别，该问题大家可以查阅相关文档，后期会有答案

"""
x = '123456'
y = '456'
z=["d", "e", "f"]
n = x.join(y)
m = x.join(z)
print(n)
print(m)
