#https://www.acmicpc.net/problem/15683

import sys
import copy

class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

mn = float("inf")
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board_copy = []
coordinate = []

for i in range(N):
    for r in range(M):
        if board[i][r] != 0 and board[i][r] != 6:
            pair = Pair(i, r)
            coordinate.append(pair)

def one_draw(x, y, dir):
    dir %= 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if (0 <= x < N and 0 <= y < M) and board_copy[x][y] != 6:
            if board_copy[x][y] == 0:
                board_copy[x][y] = "#"
        else:
            return 

for tmp in range(4 ** len(coordinate)):
    board_copy = []
    for i in range(N):
        board_copy.append([])
        for r in range(M):
            board_copy[i].append(board[i][r])

    brute = tmp
    for i in range(len(coordinate)):
        dir = brute % 4
        brute //= 4
        x = coordinate[i].x 
        y = coordinate[i].y

        if board[x][y] == 1:
            one_draw(x, y, dir)
        elif board[x][y] == 2:
            one_draw(x, y, dir)
            one_draw(x, y, dir + 2)
        elif board[x][y] == 3:
            one_draw(x, y, dir)
            one_draw(x, y, dir + 1)
        elif board[x][y] == 4:
            one_draw(x, y, dir)
            one_draw(x, y, dir + 1)
            one_draw(x, y, dir + 2)
        else:
            one_draw(x, y, dir)
            one_draw(x, y, dir + 1)
            one_draw(x, y, dir + 2)
            one_draw(x, y, dir + 3)
    
    val = 0
    for i in range(N):
        for r in range(M):
            if board_copy[i][r] == 0:
                val += 1
    mn = min(val, mn)

print(mn)
