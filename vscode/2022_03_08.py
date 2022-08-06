#https://www.acmicpc.net/problem/2399
import sys
a = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))
result = 0
c = 0
for i in range(0, a):
    for r in range(i, a):
        c = abs(b[i] - b[r])
        result += c
print(result * 2)

#https://www.acmicpc.net/problem/7785
from ntpath import join
import sys

a = int(input())
li = []
re_li = []
for i in range(0, a):
    b = sys.stdin.readline().split()
    li.append(b)
for i in range(0, a):
    if li[i][1] == "enter":
        re_li.append(li[i][0])
    elif li[i][1] == "leave":
        re_li.remove(li[i][0])
re_li = sorted(re_li)
re_li.reverse()
print("\n".join(re_li))

#https://www.acmicpc.net/problem/2581
def is_number(n):
    for i in range(2, n//2 +1):
        if n % i ==0:
            return False
    return True

a = int(input())
b = int(input())
li = []
for i in range(a, b+1):
    if is_number(i):
        li.append(i)
if li == []:
    print(-1)
elif 1 in li and len(li) >= 2:
    li.remove(1)
    print(sum(li))
    print(li[0])
elif 1 in li and len(li) == 1:
    print(-1)
else:
    print(sum(li))
    print(li[0])

#https://www.acmicpc.net/problem/1065
a = int(input())
lili = []
for i in range(1, a+1):
    b = str(i)
    c = len(b)
    li = []
    for r in range(0, c-1):
        d = int(b[r+1]) - int(b[r])
        li.append(d)
    e = set(li)
    if len(e) == 1:
        lili.append(e.pop())
if a == 1:
    print(1)
elif a < 10:
    print(a)
else:
    print(len(lili)+9)
