#https://www.acmicpc.net/problem/11659
import sys

M, N = map(int, sys.stdin.readline().split())
arr = [0]
arr.extend(list(map(int, sys.stdin.readline().split())))
for i in range(2, M + 1):
    arr[i] = arr[i] + arr[i - 1]

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    print(arr[end] - arr[start - 1])

#https://www.acmicpc.net/problem/17626
import math

N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = i
    for r in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - r * r] + 1)
print(dp[N])

#https://www.acmicpc.net/problem/9375
import sys
T = int(input())

for i in range(T):
    N = int(input())
    costumes = {}
    for r in range(N):
        costume = list(map(str, sys.stdin.readline().split()))
        if costume[1] in costumes:
            costumes[costume[1]] += 1
        else:
            costumes[costume[1]] = 2
    
    cnt = 1
    for r in costumes.values():
        cnt *= r
    print(cnt - 1)


#https://www.acmicpc.net/problem/2110
import sys

N, C = map(int, sys.stdin.readline().split())
router = []
for i in range(N):
    router.append(int(sys.stdin.readline()))
router.sort()

start = 0
end = router[-1] - router[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    cnt = 1
    current = router[0]
    for i in range(1, len(router)):
        if router[i] >= current + mid:
            cnt += 1
            current = router[i]
    
    if cnt < C:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

#https://www.acmicpc.net/problem/2512
import sys
N = int(input())
budgets = list(map(int, sys.stdin.readline().split()))
total = int(input())

if sum(budgets) < total:
    print(max(budgets))
else:
    budgets.sort()
    start = 0
    end = budgets[-1]
    result = 0
    while (start <= end):
        mid = (start + end) // 2
        total_budget = sum(budget if budget < mid else mid for budget in budgets)
        if total_budget <= total:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)

#https://www.acmicpc.net/problem/3944
import sys
T = int(sys.stdin.readline())
for i in range(T):
    B, D = map(str, sys.stdin.readline().split())
    D = sum(map(int, list(D)))
    print(D % (int(B) - 1))

#https://www.acmicpc.net/problem/2089
N = int(input())

binary = ''
while (N != 0):
    if N % 2:
        binary += '1'
        N = N // -2 + 1
    else:
        binary += '0'
        N //= -2
print(binary[::-1] if binary != '' else '0')
