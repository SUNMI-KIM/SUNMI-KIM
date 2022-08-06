#https://www.acmicpc.net/problem/2355
import sys

a = sys.stdin.readline().split()
if int(a[0]) < int(a[1]):
    b, c = int(a[0]), int(a[1])
else:
    b, c = int(a[1]), int(a[0])
if b == 1:
    print(c*(c+1)//2)
else:
    print((c*(c+1)//2)-(b*(b-1)//2))

#https://www.acmicpc.net/problem/2386
a = input().lower()
b = len(a)
li = []
while True:
    if a == "#":
        break
    li.append(a[0] +" "+str(a[1:].count(a[0])))
    a = input().lower()
    b = len(a)
for i in range(0, len(li)):
    print(li[i])

#https://www.acmicpc.net/problem/2420
a = input().split()
print(abs(int(a[0])-int(a[1])))
