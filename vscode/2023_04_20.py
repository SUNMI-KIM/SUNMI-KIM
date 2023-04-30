#https://www.acmicpc.net/problem/1793
import sys

Rectangle = [1] * (251)
Rectangle[1], Rectangle[2] = 1, 3
for i in range(3, 251):
    Rectangle[i] = Rectangle[i - 1] + Rectangle[i - 2] * 2 

while True:
    try:
        n = int(input())
        print(Rectangle[n])
    except:
        break

#https://www.acmicpc.net/problem/16194
import sys

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
dp = [0]
for i in range(1, len(card) + 1):
    dp.append(card[i - 1])

for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], card[j - 1] + dp[i - j])
print(dp[N])

#https://www.acmicpc.net/problem/10844
N = int(input())
dp = [[0 for i in range(10)] for r in range(101)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for r in range(0, 10):
        if r == 0:
            dp[i][r] = dp[i - 1][1]
        elif r == 9:
            dp[i][r] = dp[i - 1][8]
        else:
            dp[i][r] = dp[i - 1][r - 1] + dp[i - 1][r + 1]
print(sum(dp[N]) % 1000000000)

