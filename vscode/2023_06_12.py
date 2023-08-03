#https://www.acmicpc.net/problem/7569

import sys
from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, sys.stdin.readline().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dist = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue = deque()

for i in range(H):
    for r in range(N):
        for k in range(M):
            if tomato[i][r][k] == 1:
                queue.appendleft((i, r, k))
            elif tomato[i][r][k] == 0:
                dist[i][r][k] = -1

while queue:
    z, x, y = queue.pop()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
            continue
        if dist[nz][nx][ny] >= 0:
            continue
        dist[nz][nx][ny] = dist[z][x][y] + 1
        queue.appendleft((nz, nx, ny))

def print_tomato():
    ans = 0
    for i in range(H):
        for r in range(N):
            for k in range(M):
                if dist[i][r][k] == -1:
                    print(-1)
                    return 0
                ans = max(ans, dist[i][r][k])
    print(ans)
    return 0

'''def print_arr(arr):
    for i in range(len(arr)):
        print(i)
        for r in range(len(arr[i])):
            for k in range(len(arr[i][r])):
                print(arr[i][r][k], end = " ")
            print()'''

print_tomato()