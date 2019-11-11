# -*- coding:utf-8 -*-
def countdown(i):
    print(i)
    if i <=0:
        return
    else:
        countdown(i-1)

if __name__ == '__main__':
    print(countdown(3))
