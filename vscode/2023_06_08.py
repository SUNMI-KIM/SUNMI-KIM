#https://www.acmicpc.net/problem/1697

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
dir = [-1, +1]
board = [-1] * 100001
board[N] = 0
queue = deque()
queue.append(N)

while board[K] == -1:
    cur = queue.popleft()
    for next in [cur + 1, cur - 1, cur * 2]:
        if next < 0 or next > 100000:
            continue
        if board[next] != -1:
            continue
        board[next] = board[cur] + 1
        queue.append(next)
print(board[K])

#https://www.acmicpc.net/problem/1012

import sys
from collections import deque

T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(N)] for k in range(M)]
    vis = [[0 for j in range(N)] for k in range(M)]
    queue = deque()
    worm = 0
    for r in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        board[X][Y] = 1
    for r in range(M):
        for k in range(N):
            if board[r][k] == 0 or vis[r][k]:
                continue
            worm += 1
            vis[r][k] = 1
            queue.append((r, k))
            while queue:
                x, y = queue.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] != 1 or vis[nx][ny]:
                        continue
                    vis[nx][ny] = 1
                    queue.append((nx, ny))
    print(worm)

#https://www.acmicpc.net/problem/10026

import sys
from collections import deque

N = int(input())
board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
vis = [[0 for r in range(N)] for i in range(N)]
for i in range(N):
    board.append(list(str(sys.stdin.readline().strip())))

queue = deque()
color_num = 0
for i in range(N):
    for r in range(N):
        if vis[i][r]:
            continue
        color_num += 1
        vis[i][r] = 0
        queue.append((i, r))
        color = board[i][r]
        while queue:
            x, y = queue.pop()
            for dir in range(0, 4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if vis[nx][ny] or board[nx][ny] != color:
                    continue
                queue.append((nx, ny))
                vis[nx][ny] = 1
print(color_num, end = " ")

vis = [[0 for r in range(N)] for i in range(N)]
queue.clear()
dic = {"R" : "S", "B" : "B", "G" : "S"}
color_num = 0
for i in range(N):
    for r in range(N):
        if vis[i][r]:
            continue
        color_num += 1
        vis[i][r] = 0
        queue.append((i, r))
        color = dic[board[i][r]]
        while queue:
            x, y = queue.pop()
            for dir in range(0, 4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if vis[nx][ny] or dic[board[nx][ny]] != color:
                    continue
                queue.append((nx, ny))
                vis[nx][ny] = 1
print(color_num)