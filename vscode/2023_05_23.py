#https://www.acmicpc.net/problem/2869
import sys

A, B, V = map(int, sys.stdin.readline().split())

if ((V - A) % (A - B) == 0):
    print((V - A) // (A - B) + 1)
else:
    print((V - A) // (A - B) + 2)

#https://www.acmicpc.net/problem/1654
import sys

N, K = map(int, sys.stdin.readline().split())
LANline = []
for i in range(N):
    LANline.append(int(input()))

start = 1
end = max(LANline)
result = 0

while (start <= end):
    mid = (end + start) // 2
    count = sum(cable // mid for cable in LANline)
    if count >= K:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)

#https://www.acmicpc.net/problem/2805
import sys
N, M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(woods)
result = 0

while (start <= end):
    mid = (start + end) // 2
    count = sum(wood - mid if (wood - mid > 0) else 0 for wood in woods)
    if count >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)