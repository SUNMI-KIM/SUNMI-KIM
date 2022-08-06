#https://www.acmicpc.net/problem/
import sys

a = int(input())
for i in range(0, a):
    b = sys.stdin.readline().split()
    s = 0
    n = 0
    e = len(b) - 1
    for r in range(1, e + 1):
        s += int(b[r])
    c = s / e 
    for t in range(1, e + 1):
        if int(b[t]) > c:
            n += 1
    d = round(n/e * 100, 3)
    g = str(d).split(".")
    if len(g[1]) < 3:
        f = 3 - len(g[1])
        d = str(d) + "0" * f
    else:
        d = str(d)
    print(d + "%")

#https://www.acmicpc.net/problem/11720
a = int(input())
b = str(input())
c = 0
for i in range(0, a):
    c += int(b[i])
print(c)

#https://www.acmicpc.net/problem/1259
a = str(input())
while True:
    if a == "0":
        break
    if a == a[::-1]:
        print("yes")
    else:
        print("no")
    a = str(input())

#https://www.acmicpc.net/problem/1008
import sys

a = sys.stdin.readline().split()
print(int(a[0])/int(a[1]))

#https://www.acmicpc.net/problem/2557
print("Hello World!")

#https://www.acmicpc.net/problem/1152
import sys

a = sys.stdin.readline().split()
print(len(a))

#https://www.acmicpc.net/problem/15596
def solve(a):
    return sum(a)

#https://www.acmicpc.net/problem/2743
a = input()
print(len(a))

#https://www.acmicpc.net/problem/1731
a = int(input())
li = []
for i in range(0, a):
    b = int(input())
    li.append(b)
if li[1] - li[0] == li[2] - li[1]:
    print(li[len(li)-1] + (li[1] - li[0]))
else:
    print(li[len(li)-1] * li[1] // li[0])

#https://www.acmicpc.net/problem/2576
li = []
for i in range(0, 7):
    a = int(input())
    if a % 2 != 0:
        li.append(a)
li.sort()
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])