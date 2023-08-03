#https://www.acmicpc.net/problem/1941

import sys
from collections import deque

board = [list(str(sys.stdin.readline().strip())) for _ in range(5)]
arr = []
ans = 0

def dfs(depth, cnt, start):
    if cnt >= 4:
        return
    if depth == 7:
        if bfs(arr):
            global ans
            ans += 1
        return
    
    for i in range(start, 25):
        x = i // 5
        y = i % 5
        arr.append((x, y))
        dfs(depth + 1, cnt + (board[x][y] == "Y"), i + 1)
        arr.pop()

def bfs(arr):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    isvisited = [[1 for _ in range(5)] for __ in range(5)]
    cnt = 1
    queue = deque()
    for x, y in arr:
        isvisited[x][y] = 0
    x, y = arr[0]
    isvisited[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 > nx or nx >= 5 or 0 > ny or ny >= 5:
                continue
            if isvisited[nx][ny]:
                continue
            isvisited[nx][ny] = 1
            queue.append((nx, ny))
            cnt += 1
    
    return (True if cnt == 7 else False)

dfs(0, 0, 0)
print(ans)