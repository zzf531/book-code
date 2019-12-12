from random import randint
from threading import Thread
from time import time, sleep


def mps(filename):
    print('我在%s听周杰伦的七里香...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s里面七里香听完了! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=mps, args=('网易云',))
    t1.start()
    t2 = Thread(target=mps, args=('酷狗',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()