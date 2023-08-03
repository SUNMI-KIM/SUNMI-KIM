#https://www.acmicpc.net/problem/14500

import sys

tetromino = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[1, 1, 1], [0, 1, 0]],
]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sticker = []

def rotate():
    x = len(sticker)
    y = len(sticker[0])
    result = [[0] * x for _ in range(y)]
    for i in range(x):
        for r in range(y):
            result[r][x - i - 1] = sticker[i][r]
    return result

def attach(x, y):
    ans = 0
    for i in range(len(sticker)):
            for r in range(len(sticker[i])):
                if sticker[i][r]:
                     ans += board[i + x][r + y]
    return ans

max_ans = 0
for i in range(N):
    for r in range(M):
        for l in range(5):
            sticker = tetromino[l]
            for __ in range(2):
                for _ in range(4):
                    if 0 <= i + len(sticker) -1 < N and 0 <= r + len(sticker[0]) -1 < M:
                        max_ans = max(attach(i, r), max_ans)
                    sticker = rotate()                   
                sticker = sticker[::-1]
print(max_ans)

# 백트래킹 코드
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
isvisited = [[0 for _ in range(M)] for __ in range(N)]
max_val = max(map(max, board)) # 모든 좌표 중 최댓값
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
max_ans = 0

def dfs(cnt, ans, x, y):
    global max_ans
    if ans + max_val * (4-cnt) <= max_ans:
        return

    if cnt == 4:
        max_ans = max(ans, max_ans)
        return
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if isvisited[nx][ny]:
            continue
        if cnt == 2:
            isvisited[nx][ny] = 1
            dfs(cnt + 1, ans + board[nx][ny], x, y)
            isvisited[nx][ny] = 0
        isvisited[nx][ny] = 1
        dfs(cnt + 1, ans + board[nx][ny], nx, ny)
        isvisited[nx][ny] = 0


for i in range(N):
    for r in range(M):
        isvisited[i][r] = 1
        dfs(1, board[i][r], i, r)
        isvisited[i][r] = 0

print(max_ans)