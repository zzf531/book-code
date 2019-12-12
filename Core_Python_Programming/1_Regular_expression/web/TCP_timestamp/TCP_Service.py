# -*- coding: UTF-8 -*-

from socket import *
from time import ctime

# import socket  # 导入 socket 模块

HOST = '127.0.0.7'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('等待链接')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...连接中', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        tcpCliSock.send((f"{ctime()}, {data}, {'TCP原生的'}").encode())

    tcpCliSock.close()
# tcpSerSock.close()
