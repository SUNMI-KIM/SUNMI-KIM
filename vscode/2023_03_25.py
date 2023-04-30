import sys

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.cur = self.head
    
    def add_first(self, data):
        pointer = self.head
        newNode = Node(data, None)
        self.head.next = newNode
        newNode.next = newNode
        
    def add_last(self, data):
        pointer = self.head
        if pointer.next is None:
            self.add_first(data)
        else:
            first_pointer = self.head.next
            cur_pointer = self.head.next    
            while cur_pointer.next != first_pointer:
                cur_pointer = cur_pointer.next
            cur_pointer.next = Node(data, first_pointer)

    def remove(self, p):
        if p == self.head.next:
            first_pointer = self.head.next
            self.head.next = p.next
            while (p.next != first_pointer):
                p = p.next
            p.next = self.head.next
        else:
            pointer = self.head.next
            while (pointer.next != p):
                pointer = pointer.next
            pointer.next = p.next

N, K = map(int, sys.stdin.readline().split())
Clist = CircularLinkedList()
li = []

for i in range(1, N + 1):
    Clist.add_last(i)
Clist.cur = Clist.head

for i in range(0, N):
    for r in range(0, K):
        Clist.cur = Clist.cur.next
    li.append(Clist.cur.data)
    Clist.remove(Clist.cur)

print("<", end = "")
for i in range(0, N):
    if i == N - 1:
        print(li[i], end = "")
    else:
        print(li[i], end = ", ")
print(">", end = "")

#2346
class Node:
    def __init__(self, data, index, prev, next):
        self.data = data
        self.index = index
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None, None, None)
        self.current = self.head

    def add_first(self, data, index):
        pointer = Node(data, index, None, None)
        self.head.next = pointer
        pointer.next = pointer
        pointer.prev = pointer
       
    
    def add_last(self, data, index, p):
        if p == self.head:
            self.add_first(data, index)
        else:
            newNode = Node(data, index, p, self.head.next)
            p.next = newNode
            self.head.next.prev = newNode

    def remove(self, p):
        p.prev.next = p.next
        p.next.prev = p.prev
        if p == self.head.next:
            self.head.next = p.next

import sys

N = int(input())
Dlist = DoubleLinkedList()
num = list(map(int, sys.stdin.readline().strip().split()))
ans = []

for i in range(1, N + 1):
    Dlist.add_last(i, num[i - 1], Dlist.current)
    Dlist.current = Dlist.current.next
Dlist.current = Dlist.head.next

for i in range(0, N):
    index = Dlist.current.index
    ans.append(Dlist.current.data)
    Dlist.remove(Dlist.current)
    if index < 0:
        index *= -1
        for r in range(0, index):
            Dlist.current = Dlist.current.prev
    else:
        for r in range(0, index):
            Dlist.current = Dlist.current.next

for i in ans:
    print(i, end = " ")
