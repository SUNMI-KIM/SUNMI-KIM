#https://www.acmicpc.net/problem/16987

import sys

d = [] # 내구도
w = [] # 무게 
N = int(input())
max_cnt = 0
cnt = 0
for _ in range(N):
    durability, weight = map(int, sys.stdin.readline().split())
    d.append(durability)
    w.append(weight)

def dfs(hand):
    global cnt, max_cnt
    if hand == N:
        max_cnt = max(cnt, max_cnt)
        return 
    
    if d[hand] <= 0 or cnt == N-1:
        dfs(hand + 1)
        return

    for i in range(N):
        if i == hand or d[i] <= 0:
            continue
        d[hand] -= w[i]
        d[i] -= w[hand]
        if d[hand] <= 0:
            cnt += 1
        if d[i] <= 0:
            cnt += 1
        dfs(hand + 1)
        if d[hand] <= 0:
            cnt -= 1
        if d[i] <= 0:
            cnt -= 1
        d[hand] += w[i]
        d[i] += w[hand]
            
dfs(0)
print(max_cnt)

#https://www.acmicpc.net/problem/1987

import sys
from string import ascii_uppercase

R, C = map(int, sys.stdin.readline().split())
board = [list(str(sys.stdin.readline().strip())) for _ in range(R)]
check = [0] * (26)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

max_cnt = 0

def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(cnt, max_cnt)

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if check[ord(board[nx][ny]) - 65]:
            continue
        check[ord(board[nx][ny]) - 65] = 1
        dfs(nx, ny, cnt + 1)
        check[ord(board[nx][ny]) - 65] = 0

check[ord(board[0][0]) - 65] = 1
dfs(0, 0, 1)
print(max_cnt)