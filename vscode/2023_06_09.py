#https://www.acmicpc.net/problem/5427
import sys
from collections import deque

T = int(input())

for l in range(T):
    C, R = map(int, sys.stdin.readline().split())
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
            if fire[i][r] == "*":
                fire[i][r] = 0
                move[i][r] = "#"
                fire_queue.append((i, r))
            elif fire[i][r] == ".":
                fire[i][r] = -1
                move[i][r] = -1
            elif fire[i][r] == "@":
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

#https://www.acmicpc.net/problem/7562

import sys
from collections import deque

T = int(input())
dx = [2, 1, -1, -2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

'''def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])'''

for i in range(T):
    queue = deque()
    l = int(input())
    cur_x, cur_y = map(int, sys.stdin.readline().split())
    move_x, move_y = map(int, sys.stdin.readline().split())
    vis = [[-1 for r in range(l)] for i in range(l)]
    vis[cur_x][cur_y] = 0
    queue.append((cur_x, cur_y))

    while vis[move_x][move_y] == -1:
        x, y = queue.popleft()
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if vis[nx][ny] != -1:
                continue
            vis[nx][ny] = vis[x][y] + 1
            queue.append((nx, ny))
    print(vis[move_x][move_y])