#https://www.acmicpc.net/problem/7576

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))
            dist[i][j] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

ans = max([max(row) for row in dist])

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and dist[i][j] == -1:
            ans = -1

print(ans)


#https://www.acmicpc.net/problem/4179

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = []
fire = []
move = []
for i in range(R):
    line = list(str(input()))
    board.append(line.copy())
    fire.append(line.copy())
    move.append(line.copy())
fire_queue = deque()
move_queue = deque()
ans = "IMPOSSIBLE"

for i in range(R):
    for r in range(C):
        if fire[i][r] == "F":
            fire[i][r] = 0
            move[i][r] = "#"
            fire_queue.append((i, r))
        elif fire[i][r] == ".":
            fire[i][r] = -1
            move[i][r] = -1
        elif fire[i][r] == "J":
            fire[i][r] = -1
            move[i][r] = 0
            move_queue.append((i, r))

while fire_queue:
    x, y = fire_queue.popleft()
    for dir in range(0, 4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if fire[nx][ny] == "#":
            continue
        if fire[nx][ny] >= 0:
            continue
        fire[nx][ny] = fire[x][y] + 1
        fire_queue.append((nx, ny))

flag = 1
while move_queue and flag:
    x, y = move_queue.popleft()
    for dir in range(0, 4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            ans = move[x][y] + 1
            flag = 0
            break
        if move[nx][ny] == "#" or move[nx][ny] >= 0:
            continue
        if move[x][y] + 1 >= fire[nx][ny] and fire[nx][ny] != -1:
            continue
        move[nx][ny] = move[x][y] + 1
        move_queue.append((nx, ny))

print(ans)
