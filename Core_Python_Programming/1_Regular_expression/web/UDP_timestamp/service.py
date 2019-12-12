# -*- coding: UTF-8 -*-

from socket import *
from time import ctime

HOST = '127.0.0.13'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('...等待连接...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s'%(ctime(),data)).encode(),addr)
    print('received from and returned to', addr)


