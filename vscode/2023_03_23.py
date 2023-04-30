#https://www.acmicpc.net/problem/2840
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
        
    def write(self, p, n):
        stack = []
        print(p.data, end = "")
        p = p.next
        for i in range(0, n - 1):
            stack.append(p.data)
            p = p.next
        while (len(stack) != 0):
            print(stack.pop(), end = "")

Clist = CircularLinkedList()
dic = {}
status = 1
N, K = map(int, sys.stdin.readline().split())
for i in range(0, N):
    Clist.add_last("?")

for i in range(0, K):
    S, string = map(str, sys.stdin.readline().split())
    S = int(S)
    for num in range(0, S):
        Clist.cur = Clist.cur.next
    if (Clist.cur.data.isalpha() and Clist.cur.data != string) or (Clist.cur.data != string and string in dic):
        status = 0
    else:
        Clist.cur.data = string
        dic[string] = string
if status == 1:
    Clist.write(Clist.cur, N)
elif status == 0:
    print("!")