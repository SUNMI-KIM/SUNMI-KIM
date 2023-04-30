#https://www.acmicpc.net/problem/9461
T = int(input())
dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2 

for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for i in range(T):
    print(dp[int(input())])

#https://www.acmicpc.net/problem/2156
n = int(input())
wine = [0]
dp = [0] * (n + 1)
for i in range(n):
    wine.append(int(input()))

dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    dp[i] = dp[i - 1]
    dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i],  dp[i - 2] + wine[i], dp[i])
print(dp[n])