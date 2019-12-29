"""
1.链式比较
"""
i = 3
print(1 < i < 3)
print(1 < i <= 3)  # True


"""
2 不用else和if实现计算器
"""


from operator import *


def calculator(a, b, k):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '**': pow
    }[k](a, b)


print(calculator(1, 2, '+'))

