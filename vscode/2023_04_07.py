#https://www.acmicpc.net/problem/1010
import sys
import math
T = int(input())

for i in range(T):
    M, N = map(int, sys.stdin.readline().strip().split())
    print(math.comb(N, M))

#https://www.acmicpc.net/problem/1463
N = int(input())

l = [0] * (N + 1)

for i in range(2, N + 1):
    l[i] = l[i - 1] + 1
    if i % 3 == 0:
        l[i] = min(l[i], l[i // 3] + 1)
    if i % 2 == 0:
        l[i] = min(l[i], l[i // 2] + 1)

print(l[N])

#https://www.acmicpc.net/problem/9095
T = int(input())

l = [0] * 12
l[1], l[2], l[3] = 1, 2, 4

for i in range(4, 12):
    l[i] = l[i - 1] + l[i - 2] + l[i - 3]

for i in range(T):
    print(l[int(input())])

#https://www.acmicpc.net/problem/2579
N = int(input())

stair = [0] * 301
dp = [0] * 301
for i in range(1, N + 1):
    stair[i] = int(input())

dp[1], dp[2] = stair[1], stair[2] + stair[1]
dp[3] = max(stair[2] + stair[3], stair[1] + stair[3])

for i in range(4, N + 1):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[N])