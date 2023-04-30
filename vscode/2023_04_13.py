##https://www.acmicpc.net/problem/11727
n = int(input())
Rectangle = [0] * (1001)

Rectangle[1], Rectangle[2] = 1, 3

for i in range(3, n + 1):
    Rectangle[i] = Rectangle[i - 1] + Rectangle[i - 2] * 2 

print(Rectangle[n] % 10007)

#https://www.acmicpc.net/problem/1912
import sys
n = int(input())
sequence = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * n
dp[0] = sequence[0]

for i in range(1, n):
    dp[i] = max(sequence[i], dp[i - 1] + sequence[i])

print(max(dp))

#https://www.acmicpc.net/problem/1699
import math
N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = i # 1로만 나타내기
    for r in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - r * r] + 1)
print(dp[N])
