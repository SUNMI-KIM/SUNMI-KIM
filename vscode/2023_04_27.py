#https://www.acmicpc.net/problem/2002
N = int(input())
enter = {}
out = []
overtake = 0

for i in range(0, N):
    enter[input()] = i

for i in range(0, N):
    out.append(enter[input()])

for i in range(0, N):
    for r in range(i, N):
        if out[i] > out[r]:
            overtake += 1
            break
print(overtake)

#https://www.acmicpc.net/problem/22233
import sys

N, M = map(int, sys.stdin.readline().split())
memo = {}


for i in range(0, N):
    memo[sys.stdin.readline().strip()] = 1 

for i in range(0, M):
    keyword = list(map(str, sys.stdin.readline().strip().split(",")))
    for kw in keyword:
        if kw in memo and memo[kw] == 1:
            memo[kw] -= 1
            N -= 1
    print(N)

#https://www.acmicpc.net/problem/1789
S = int(input())
N = 0

for i in range(1, S + 1):
    if S - i >= i + 1:
        S -= i
        N += 1
    elif S - i == 0:
        N += 1
        break
print(N)

#https://www.acmicpc.net/problem/2407
import sys

def factorial(number):
    ans = 1
    for i in range(2, number + 1):
        ans *= i
    return ans

n, m = map(int, sys.stdin.readline().split())
print(factorial(n) // (factorial(m) * factorial(n - m)))