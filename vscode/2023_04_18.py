#https://www.acmicpc.net/problem/9996
N = int(input())
pattern = input()
starIndex = pattern.find("*")

for i in range(0, N):
    flag = 1
    file = input()
    if len(pattern) - 1 > len(file):
        flag = 0
    if flag == 1:
        for r in range(0, starIndex):
            if file[r] != pattern[r]:
                flag = 0
                break
    if flag == 1:
        index = len(pattern) - 1
        for r in range(len(file) - 1, len(file) - (len(pattern) - 1 - starIndex) - 1, -1):
            if pattern[index] == "*":
                break
            if file[r] != pattern[index]:
                flag = 0
                break
            index -= 1
    if flag == 0:
        print("NE")
    else:
        print("DA")

#https://www.acmicpc.net/problem/1965
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * N

for i in range(N):
    for r in range(i - 1, -1, -1):
        if A[i] > A[r]:
            dp[i] = max(dp[r] + 1, dp[i])
print(max(dp))

#https://www.acmicpc.net/problem/15486
import sys
N = int(input())
t = [0] * (N + 1)
p = [0] * (N + 1)
dp = [0] * (N + 2)

for i in range(1, N + 1):
    t[i], p[i] = map(int, sys.stdin.readline().strip().split())

for i in range(1, N + 1):
    dp[i] = max(dp[i - 1], dp[i])
    if i + t[i] <= N + 1:
        dp[i + t[i]] = max(dp[i] + p[i], dp[t[i] + i])
print(dp[N])