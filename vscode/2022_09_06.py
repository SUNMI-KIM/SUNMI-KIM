#https://www.acmicpc.net/problem/1500
import sys
num, length = map(int, sys.stdin.readline().split())

a = round(num/length)
li = []

for i in range(0, length):
    li.append(a)

b = sum(li)
c = num - b
if c > 0:
    for i in range(0, c):
        li[i] += 1
elif c < 0:
    for i in range(0, abs(c)):
        li[i] -= 1

result = 1
for i in li:
    result *= i
print(result)
    