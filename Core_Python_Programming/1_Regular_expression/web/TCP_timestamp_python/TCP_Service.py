# -*- coding: UTF-8 -*-

from socket import *
from time import ctime

HOST = '127.0.0.13'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('等待连接')
    tcpCliSock, addr = tcpSerSock.accept()
    print('连接地址', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        # tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.send((f"{ctime()}, {data}, {'python3TCP'}").encode())
    tcpCliSock.close()
