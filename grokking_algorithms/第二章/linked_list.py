# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
b = ListNode(4)
c = ListNode(9)
a.next = b
b.next = c

while a:
    print(a.val)
    a = a.next
