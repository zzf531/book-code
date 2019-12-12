# -*- coding: UTF-8 -*-

from socket import *

HOST = '::13'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClisock = socket(AF_INET6, SOCK_STREAM)
tcpClisock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpClisock.send(data.encode())
    data = tcpClisock.recv(BUFSIZ)
    if not data:
        break
    print(data)
tcpClisock.close()