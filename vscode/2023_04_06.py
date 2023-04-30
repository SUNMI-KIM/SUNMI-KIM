#https://www.acmicpc.net/problem/2503
import sys
N = int(input())

li = []
ans = 0
for i in range(0, N):
    li.append(list(map(str, sys.stdin.readline().strip().split())))

for i in range(123, 988):
    compare = 0
    strBox = list(set(str(i)))
    if len(strBox) == 3 and strBox[0] != '0' and strBox[1] != '0' and strBox[2] != '0':
        for r in range(0, N):
            strike = 0
            ball = 0
            strBox = list(set(str(i)))
            if len(strBox) != 3:
                break
            for l in range(0, 3):
                if str(i)[l] == li[r][0][l]:
                    strike += 1
            
            for l in range(0, len(strBox)):
                ball += li[r][0].count(strBox[l])

            ball = ball - strike
            if int(li[r][1]) == strike and int(li[r][2]) == ball:
                compare += 1
            else:
                break
        if compare == N:
            ans += 1
print(ans)

#https://www.acmicpc.net/problem/4796
import sys

L, P, V = map(int, sys.stdin.readline().strip().split())
date = 1
while (L != 0 and P != 0 and V != 0):
    vacation = 0
    while (V > 0):
        if V - L >= 0:
            V -= L
            vacation += L
            if V - (P - L) > 0:
                V -= (P - L)
            else:
                break
        else:
            vacation += V
            break
    print("Case %d: %d" %(date, vacation))
    date += 1     
    L, P, V = map(int, sys.stdin.readline().strip().split()) 

#https://www.acmicpc.net/problem/1449
import sys
N, L = map(int, sys.stdin.readline().strip().split())
repair = sorted(list(map(int, sys.stdin.readline().strip().split())))
repairNum = 1
cover = repair[0] + (L - 1)
for i in range(1, N):
    if cover >= repair[i]:
        continue
    else:
        repairNum += 1
        cover = repair[i] + (L - 1)
print(repairNum)

#https://www.acmicpc.net/problem/11047
import sys
N, K = map(int, sys.stdin.readline().strip().split())
coin = []
for i in range(N):
    coinValue = int(input())
    coin.append(coinValue)

num = 0
index = len(coin) - 1
while (K > 0):
    if K // coin[index] > 0:
        num += K // coin[index]
        K -= (coin[index] * (K // coin[index]))
    else:
        index -= 1
print(num)

#https://www.acmicpc.net/problem/1931
import sys
N = int(input())
time = []
for i in range(N):
    time.append(list(map(int, sys.stdin.readline().strip().split())))
time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

num = 1
start = time[0][1]
for i in range(1, N):
    if time[i][0] >= start:
        num += 1
        start = time[i][1]
print(num)

#https://www.acmicpc.net/problem/1018
import sys

def check(chess, x, y):
    char = 'W'
    repair = 0
    for i in range(x, x + 8):
        for r in range(y, y + 8):
            if char != chess[i][r]:
                repair += 1
            if char == 'W':
                char = "B"
            else:
                char = "W"
        if char == 'W':
                char = "B"
        else:
            char = "W"
    return repair

N, M = map(int, sys.stdin.readline().strip().split())

Chess = []
for i in range(0, N):
    Chess.append(input())

ans = []
for i in range(0, N - 7):
    for r in range(0, M - 7):
        checkNum = check(Chess, i, r)
        if checkNum > 64 - checkNum:
            ans.append(64 - checkNum)
        else:
            ans.append(checkNum)
print(min(ans))