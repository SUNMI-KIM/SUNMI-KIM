#https://www.acmicpc.net/problem/10845
import sys

class Queue():
    def __init__(self):
        self.queue = []
        self.index = 0
        self.length = 0
    
    def ft_push(self, X):
        self.queue.append(X)
        self.length += 1

    def ft_pop(self):
        if self.length - self.index < 1:
            print(-1)
        else:
            print(self.queue[self.index])
            self.index += 1
    
    def ft_size(self):
        print(self.length - self.index)

    def ft_empty(self):
        if self.length - self.index < 1:
            print(1)
        else:
            print(0)

    def ft_front(self):
        if self.length - self.index < 1:
            print(-1)
        else:
            print(self.queue[self.index])

    def ft_back(self):
        if self.length - self.index < 1:
            print(-1)
        else:
            print(self.queue[self.length - 1])

N = int(input())
queue = Queue()

for i in range(0, N):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == "push":
        queue.ft_push(int(command[1]))
    elif command[0] == "front":
        queue.ft_front()
    elif command[0] == "back":
        queue.ft_back()
    elif command[0] == "size":
        queue.ft_size()
    elif command[0] == "empty":
        queue.ft_empty()
    else:
        queue.ft_pop()

#https://www.acmicpc.net/problem/2164
from collections import deque

N = int(input())
queue = deque()

for i in range(0, N):
    queue.append(i + 1)

while (len(queue) != 1):
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())
print(queue.popleft())

#https://www.acmicpc.net/problem/1966
class Queue():
    def __init__(self, queue):
        self.queue = queue
        self.index = 0
        self.length = len(queue)
    
    def ft_push(self, X):
        self.queue.append(X)
        self.length += 1

    def ft_pop(self):
        if self.length - self.index < 1:
            return -1
        else:
            self.index += 1
            return self.queue[self.index - 1]
    
    def ft_size(self):
        return self.length - self.index

    def ft_front(self):
        if self.length - self.index < 1:
            return -1
        else:
            return self.queue[self.index]
    
    def search(self):
        for i in range(self.index + 1, self.length):
            if self.queue[self.index] < self.queue[i]:
                return False
        return True

import sys

num = int(input())

for i in range(0, num):
    N, M = map(int, sys.stdin.readline().split())
    queue = Queue(list(map(int, sys.stdin.readline().strip().split())))
    ans = 0
    while (1):
        if M == 0:
            if queue.search():
                ans += 1
                break
            else:
                queue.ft_push(queue.ft_pop())
                M = queue.ft_size() - 1
        else:
            if queue.search():
                queue.ft_pop()
                ans += 1
                M -= 1
            else:
                queue.ft_push(queue.ft_pop())
                M -= 1
    print(ans)
    
#https://www.acmicpc.net/problem/10866
class Node():
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev

class Deque():
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.length = 0
    
    def ft_push_front(self, X):
        if self.length == 0:
            newNode = Node(X, self.head, self.tail)
            self.head.next = newNode
            self.tail.prev = newNode
            self.length += 1
        else:
            newNode = Node(X, self.head, self.head.next)
            self.head.next = newNode
            newNode.next.prev = newNode
            self.length += 1
    
    def ft_push_back(self, X):
        if self.length == 0:
            newNode = Node(X, self.head, self.tail)
            self.head.next = newNode
            self.tail.prev = newNode
            self.length += 1
        else:
            newNode = Node(X, self.tail.prev, self.tail)
            self.tail.prev = newNode
            newNode.prev.next = newNode
            self.length += 1

    def ft_size(self):
        print(self.length)
    
    def ft_empty(self):
        if self.length == 0:
            print(1)
        else:
            print(0)
    
    def ft_front(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.head.next.data)
    
    def ft_back(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.tail.prev.data)

    def ft_pop_front(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.head.next.data)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.length -= 1

    def ft_pop_back(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.tail.prev.data)
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.length -= 1
    
import sys

N = int(input())
deque = Deque()

for i in range(0, N):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if command[0] == "push_front":
        deque.ft_push_front(int(command[1]))
    elif command[0] == "push_back":
        deque.ft_push_back(int(command[1]))
    elif command[0] == "pop_front":
        deque.ft_pop_front()
    elif command[0] == "pop_back":
        deque.ft_pop_back()
    elif command[0] == "size":
        deque.ft_size()
    elif command[0] == "empty":
        deque.ft_empty()
    elif command[0] == "front":
        deque.ft_front()
    else:
        deque.ft_back()