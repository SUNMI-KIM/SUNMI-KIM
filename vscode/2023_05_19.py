#https://www.acmicpc.net/problem/1436
N = int(input())
first = 666
while (N != 0):
    if "666" in str(first):
        N -= 1
        if N == 0:
            break
    first += 1
print(first)

#https://www.acmicpc.net/problem/7568
N = int(input())
information = []
for i in range(0, N):
    information.append(list(map(int, input().split())))

for i in range(0, N):
    rank = 0
    for r in range(0, N):
        if i == r:
            continue
        elif information[i][0] < information[r][0] and information[i][1] < information[r][1]: 
            rank += 1
    print(rank + 1, end = " ")

#https://www.acmicpc.net/problem/11651
import sys

N = int(input())

coordinate = []
for i in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().split())))

coordinate.sort(key = lambda x : (x[1], x[0]))
for i in range(N):
    print(coordinate[i][0], coordinate[i][1])

#https://www.acmicpc.net/problem/2839
N = int(input())
count = 0

while (N >= 0):
    if (N % 5 == 0):
        count += N // 5
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1) 

#https://www.acmicpc.net/problem/4949
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
            return True
        else:
            return False
    
    def ft_top(self):
        if self.length < 1:
            return -1
        else:
            return self.stack[self.length - 1]

while (1):
    string = input()
    if string == ".":
        break
    stack = Stack()
    for c in string:
        if c == "(" or c == "[":
            stack.ft_push(c)
        elif c == ")" and stack.ft_top() == "(":
            stack.ft_pop()
        elif c == "]" and stack.ft_top() == "[":
            stack.ft_pop()
        elif c == "]" or c == ")":
            stack.ft_push(c)
            break
    if stack.ft_empty():
        print("yes")
    else:
        print("no")