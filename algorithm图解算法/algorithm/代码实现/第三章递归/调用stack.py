# -*- coding:utf-8 -*-
def greet(name):
    print('hello,' + name + '!')
    greet2(name)
    print('getting ready to say bye')  # 准备说再见
    bye()


def greet2(name):
    print(" How are you" + name + "?")


def bye():
    print('ok bye')


if __name__ == '__main__':
    print(greet('蔡玲玲'))
