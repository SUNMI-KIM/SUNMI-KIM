#https://www.acmicpc.net/problem/10828
class Stack():
    def __init__(self):
        self.stack = []
        self.length = 0

    def ft_pop(self):
        if self.length < 1:
            print(-1)
        else:
            print(self.stack.pop())
            self.length -= 1
    
    def ft_push(self, data):
        self.stack.append(data)
        self.length += 1

    def ft_size(self):
        print(self.length)
    
    def ft_empty(self):
        if self.length < 1:
            print(1)
        else:
            print(0)
    
    def ft_top(self):
        if self.length < 1:
            print(-1)
        else:
            print(self.stack[self.length - 1])

import sys

stack = Stack()
N = int(input())
for i in range(0, N):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if command[0] == "push":
        stack.ft_push(int(command[1]))
    elif command[0] == "top":
        stack.ft_top()
    elif command[0] == "size":
        stack.ft_size()
    elif command[0] == "empty":
        stack.ft_empty()
    else:
        stack.ft_pop()

#https://www.acmicpc.net/problem/3986
import sys
N = int(input())
ans = 0

for i in range(0, N):
    string = list(str(input()))
    stack = []
    for char in string:
        if len(stack) > 0 and char == stack[len(stack) - 1]:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) == 0:
        ans += 1
print(ans)

#https://www.acmicpc.net/problem/2841

import sys
class Stack():
    def __init__(self):
        self.stack = []
        self.length = 0

    def ft_pop(self):
        if self.length < 1:
            return -1
        else:
            self.length -= 1
            return self.stack.pop()
    
    def ft_push(self, data):
        self.stack.append(data)
        self.length += 1

    def ft_size(self):
        return self.length
    
    def ft_empty(self):
        if self.length < 1:
            return 1
        else:
            return 0
    
    def ft_top(self):
        if self.length < 1:
            return -1
        else:
            return self.stack[self.length - 1]

N, P = map(int, sys.stdin.readline().split())
stack = []
ans = 0

for r in range(0, 6):
    stack.append(Stack())

for i in range(0, N):
    num, fret = map(int, sys.stdin.readline().split())
    if stack[num - 1].ft_top() < fret:
        stack[num - 1].ft_push(fret)
        ans += 1
    elif stack[num - 1].ft_top() > fret:
        while (stack[num - 1].ft_top() > fret):
            stack[num - 1].ft_pop()
            ans += 1
        if stack[num - 1].ft_top() != fret:
            stack[num - 1].ft_push(fret)
            ans += 1
print(ans)