#https://www.acmicpc.net/problem/18808

import sys

N, M, K = map(int, sys.stdin.readline().split())
board = []
sticker = []
for i in range(N):
    board.append([])
    for r in range(M):
        board[i].append(0)


def check(x, y):
    for i in range(len(sticker)):
        for r in range(len(sticker[i])):
            if board[i + x][r + y] + sticker[i][r] > 1:
                return False
    return True


def attach(x, y):
    for i in range(len(sticker)):
        for r in range(len(sticker[i])):
            board[i + x][r + y] += sticker[i][r]


def rotate():
    x = len(sticker)
    y = len(sticker[0])
    result = [[0] * x for _ in range(y)]
    for i in range(x):
        for r in range(y):
            result[r][x - i - 1] = sticker[i][r]
    return result


for i in range(K):
    flag = 0
    sticker = []
    s_x, s_y = map(int, sys.stdin.readline().split())
    for r in range(s_x):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    for _ in range(4):
        for x in range(N - len(sticker) + 1):
            for y in range(M - len(sticker[0]) + 1):
                if check(x, y) and flag == 0:
                    flag = 1
                    attach(x, y)
                    break
        if flag == 1:
            break
        sticker = rotate()

ans = 0
for i in range(len(board)):
    for r in range(len(board[i])):
        if board[i][r] == 1:
            ans += 1
print(ans)

#https://www.acmicpc.net/problem/12100

# 배열 돌리는 함수

# 그쪽으로 합치는 함수