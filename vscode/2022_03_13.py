#https://www.acmicpc.net/problem/8958
import sys

a = int(input())
li = []
for i in range(0, a):
    b = sys.stdin.readline()
    n = 0
    c = 0
    result = 0
    while n <= len(b) - 2:
        if b[n] == 'O':
            c += 1
        elif b[n] == 'X':
            c = 0
        n += 1
        result += c
    li.append(result)
for i in range(0, a):
    print(li[i])
