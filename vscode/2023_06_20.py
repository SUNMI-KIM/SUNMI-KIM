#https://www.acmicpc.net/problem/2468

import sys
from collections import deque

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
max_ans = [0]

for i in range(0, 101):
    vis = [[0 for __ in range(N)] for _ in range(N)]
    ans = 0
    for r in range(N):
        for k in range(N):
            if board[r][k] <= i or vis[r][k]:
                continue
            ans += 1
            queue = deque()
            vis[r][k] = 1
            queue.appendleft((r, k))
            while queue:
                x, y = queue.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] <= i or vis[nx][ny]:
                        continue
                    vis[nx][ny] = 1
                    queue.append((nx, ny))
    max_ans.append(ans)
    
print(max(max_ans))

#https://www.acmicpc.net/problem/6593

import sys
from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if not L:
        break
    board = []
    vis = []
    for _ in range(L):
        vis.append([])
        board.append([])
        for __ in range(R):
            board[_].append(list(str(sys.stdin.readline().strip())))
            vis[_].append([-1] * C)
        sys.stdin.readline()
    Ez, Ex, Ey= 0, 0, 0
    queue = deque()
    for i in range(L):
        for r in range(R):
            for k in range(C):
                if board[i][r][k] == "S":
                    queue.appendleft((i, r, k))
                    vis[i][r][k] = 0
                elif board[i][r][k] == "E":
                    Ez, Ex, Ey = i, r, k
    
    while queue:
        z, x, y = queue.popleft()
        for dir in range(6):
            nz = z + dz[dir]
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nz < 0 or nz >= L or nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nz][nx][ny] == "#" or vis[nz][nx][ny] >= 0:
                continue
            vis[nz][nx][ny] = vis[z][x][y] + 1
            queue.append((nz, nx, ny))
    print("Escaped in %d minute(s)." %(vis[Ez][Ex][Ey]) if vis[Ez][Ex][Ey] > 0 else "Trapped!")