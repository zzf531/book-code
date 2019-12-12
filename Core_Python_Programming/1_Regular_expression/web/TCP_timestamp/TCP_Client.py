# -*- coding: UTF-8 -*-

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClisock = socket(AF_INET, SOCK_STREAM)
tcpClisock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpClisock.send(data.encode())
    data = tcpClisock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)
tcpClisock.close()