#https://www.acmicpc.net/problem/2193
a = int(input())
cur, next = 0, 1
sum = 0
if a == 1:
    print(1)
elif a == 2:
    print(1)
elif a == 0:
    print(0)
else:
    for i in range(1, a):
        sum = (cur + next) 
        cur, next = next, sum
    print(sum)

#https://www.acmicpc.net/problem/3273
import sys
a = int(input())
b = sorted(list(map(int, sys.stdin.readline().split())))
c = int(input())

idx_left = 0
idx_right = len(b)-1
count = 0
while (idx_left < idx_right):
    if b[idx_left] + b[idx_right] == c:
        idx_left += 1
        idx_right -= 1
        count += 1
    elif b[idx_left] + b[idx_right] < c:
        idx_left += 1
    else:
        idx_right -= 1
print(count)   