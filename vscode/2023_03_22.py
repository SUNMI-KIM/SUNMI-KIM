#https://www.acmicpc.net/problem/1406
import sys

class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.current = self.tail
    
    def insert(self, data, p):
        pre = p.prev
        newNode = Node(data, pre, p)
        p.prev = newNode
        pre.next = newNode

    def delete(self, p):
        pre = p.prev
        nex = p.next
        pre.next = nex
        nex.prev = pre          

    def write(self):
        pointer = self.head.next
        while (pointer != self.tail):
            if pointer.next != self.tail:
                print(pointer.data, end="")
            else:
                print(pointer.data)
            pointer = pointer.next

string = sys.stdin.readline().rstrip('\n')
doublelinkedlist = DoubleLinkedList()
num = int(sys.stdin.readline().rstrip('\n'))

for i in range(0, len(string)):
    doublelinkedlist.insert(string[i], doublelinkedlist.tail)

for i in range(0, num):
    input = list(map(str, sys.stdin.readline().split()))
    if (input[0] == "P"):
        doublelinkedlist.insert(input[1], doublelinkedlist.current)
    elif (input[0] == "L"):
        if doublelinkedlist.current.prev.prev != None:
            doublelinkedlist.current = doublelinkedlist.current.prev
    elif (input[0] == "D"):
        if doublelinkedlist.current.next != None:
            doublelinkedlist.current = doublelinkedlist.current.next
    elif (input[0] == "B" and doublelinkedlist.current.prev.prev != None):
        doublelinkedlist.delete(doublelinkedlist.current.prev)
doublelinkedlist.write()

#https://www.acmicpc.net/problem/5397
import sys

class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.current = self.tail
    
    def insert(self, data, p):
        pre = p.prev
        newNode = Node(data, pre, p)
        p.prev = newNode
        pre.next = newNode

    def delete(self, p):
        pre = p.prev
        nex = p.next
        pre.next = nex
        nex.prev = pre          

    def write(self):
        pointer = self.head.next
        while (pointer != self.tail):
            if pointer.next != self.tail:
                print(pointer.data, end="")
            else:
                print(pointer.data)
            pointer = pointer.next

num = int(input())
for i in range(0, num):
    password = input()
    Dlist = DoubleLinkedList()
    for c in password:
        if c == "<":
            if Dlist.current.prev.prev != None:
                Dlist.current = Dlist.current.prev
        elif c == ">":
            if Dlist.current.next != None:
                Dlist.current = Dlist.current.next
        elif c == "-":
            if Dlist.current.prev.prev != None:
                Dlist.delete(Dlist.current.prev)
        else:
            Dlist.insert(c, Dlist.current)
    Dlist.write()
