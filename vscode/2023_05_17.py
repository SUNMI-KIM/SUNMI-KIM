#https://www.acmicpc.net/problem/1978
import math 

sifter = [1] * (1001)
sifter[0], sifter[1] = 0, 0
for i in range(2, int(math.sqrt(1001))):
    if sifter[i] == 1: 
        for r in range(i + i, 1001, i):
            sifter[r] = 0

N = int(input())
find = map(int, input().split())
num = 0

for i in find:
    if sifter[i] == 1:
        num += 1
print(num)

#https://www.acmicpc.net/problem/4153
while True:
    triangle = list(map(int, input().split()))
    if (triangle[0] == 0):
        break
    triangle.sort()
    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        print("right")
    else:
        print("wrong")

#https://www.acmicpc.net/problem/10250
T = int(input())

for i in range(0, T):
    H, W, N = map(int, input().split())
    roomNum = 1
    
    while (N - H > 0):
        N = N - H
        roomNum += 1
    floor = str(N)
    roomNum = str(roomNum)

    if int(roomNum) < 10:
        roomNum = "0" + roomNum
    
    print(floor + roomNum)

#https://www.acmicpc.net/problem/2798
import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

maxSum = 0

for i in range(0, N - 2):
    for r in range(i + 1, N - 1):
        for l in range(r + 1, N):
            if card[i] + card[r] + card[l] <= M:
                maxSum = max(maxSum, card[i] + card[r] + card[l])

print(maxSum)

#https://www.acmicpc.net/problem/2609
def gcd(x, y):
    while (y > 0):
        tmp = x
        x = y
        y = tmp % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

A, B = map(int, input().split())
if A < B:
    A, B = B, A

print(gcd(A, B))
print(lcm(A, B))

#https://www.acmicpc.net/problem/11050
def factorial(x):
    ans = 1
    while (x > 0):
        ans *= x
        x -= 1
    return ans

N, K = map(int, input().split())

print(factorial(N) // (factorial(K) * factorial(N - K)))

#https://www.acmicpc.net/problem/2751
import sys
N = int(input())
num = []

for i in range(N):
    num.append(int(sys.stdin.readline().strip()))

num.sort()
for i in num:
    print(i)

#https://www.acmicpc.net/problem/10814
import sys

N = int(input())
user = []
for i in range(N):
    user.append(list(map(str, sys.stdin.readline().split())))

for i in range(N):
    user[i][0] = int(user[i][0])

user.sort(key = lambda x:x[0])

for i in range(N):
    print(user[i][0], user[i][1])

#https://www.acmicpc.net/problem/11650
import sys

N = int(input())

coordinate = []
for i in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().split())))

coordinate.sort()
for i in range(N):
    print(coordinate[i][0], coordinate[i][1])

#https://www.acmicpc.net/problem/11866
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.current = self.head

    def add_first(self, data):
        pointer = Node(data, None, None)
        self.head.next = pointer
        pointer.next = pointer
        pointer.prev = pointer
       
    
    def add_last(self, data, p):
        if p == self.head:
            self.add_first(data)
        else:
            newNode = Node(data, p, self.head.next)
            p.next = newNode
            self.head.next.prev = newNode

    def remove(self, p):
        p.prev.next = p.next
        p.next.prev = p.prev
        if p == self.head.next:
            self.head.next = p.next

doubleLinkedList = DoubleLinkedList()
N, K = map(int, input().split())
for i in range(1, N + 1):
    doubleLinkedList.add_last(i, doubleLinkedList.current)
    doubleLinkedList.current = doubleLinkedList.current.next
doubleLinkedList.current = doubleLinkedList.head

deleteOrder = []
for i in range(N):
    for i in range(K):
        doubleLinkedList.current = doubleLinkedList.current.next
    deleteOrder.append(str(doubleLinkedList.current.data))
    doubleLinkedList.remove(doubleLinkedList.current)

print("<" + ", ".join(deleteOrder) + ">")