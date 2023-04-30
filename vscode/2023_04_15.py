#https://www.acmicpc.net/problem/11053
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * N

for i in range(N):
    for r in range(i - 1, -1, -1):
        if A[i] > A[r]:
            dp[i] = max(dp[r] + 1, dp[i])
print(max(dp))

#https://www.acmicpc.net/problem/1543
text = str(input())
search = str(input())
count = 0
i = 0

while (i <= len(text) - len(search)):
    index = 0
    for r in range(0, len(search)):
        if text[i + r] == search[r]:
            index += 1
    if index == len(search):
        count += 1
        i += (len(search))
    else:
        i += 1
print(count)