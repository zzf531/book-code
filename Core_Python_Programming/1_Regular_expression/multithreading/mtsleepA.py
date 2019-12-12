# -*- coding:utf-8 -*-
import _thread
from time import ctime, sleep

def loop0():
    print('开始 loop0 at', ctime())
    sleep(4)
    print('loop 0 完成 at', ctime())

def loop1():
    print ('开始 loop1 at:', ctime())
    sleep(1)
    print ('loop 1 完成 at:', ctime())


def main():
    print('starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(7)
    print('全部结束时间', ctime())


if __name__ == '__main__':
    main()