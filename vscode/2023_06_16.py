#https://www.acmicpc.net/problem/17298
import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def ft_pop(self):
        if self.length < 1:
            return -1
        else:
            self.length -= 1
            return self.stack.pop()

    def ft_push(self, data):
        self.stack.append(data)
        self.length += 1

    def ft_size(self):
        return self.length

    def ft_empty(self):
        if self.length < 1:
            return True
        else:
            return False

    def ft_top(self):
        if self.length < 1:
            return -1
        else:
            return self.stack[self.length - 1]


A = int(input())
N = list(map(int, sys.stdin.readline().split()))
stack = Stack()
ans = [0] * A

for i in range(A - 1, -1, -1):
    val = N[i]
    while not stack.ft_empty() and stack.ft_top() <= val:
        stack.ft_pop()
    ans[i] = stack.ft_top()
    stack.ft_push(N[i])

for i in ans:
    print(i, end=" ")


#https://www.acmicpc.net/problem/14940

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
queue = deque()

for i in range(n):
    for r in range(m):
        if board[i][r] == 2:
            queue.appendleft((i, r))
            board[i][r] = 0
        if board[i][r] == 1:
            board[i][r] = -1

while queue:
    x, y = queue.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] != -1:
            continue
        board[nx][ny] = board[x][y] + 1
        queue.append((nx, ny))

for i in range(n):
    for r in range(m):
        print(board[i][r], end = " ")
    print()


#https://www.acmicpc.net/problem/21736

import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = []
vis = []
queue = deque()
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    board.append(list(str(sys.stdin.readline().strip())))
    vis.append([-1] * M)

for i in range(N):
    for r in range(M):
        if board[i][r] == "I":
            vis[i][r] = 1
            queue.appendleft((i, r))

ans = 0

while queue:
    x, y = queue.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == "X" or vis[nx][ny] != -1:
            continue
        if board[nx][ny] == "P":
            ans += 1
        vis[nx][ny] = 1
        queue.append((nx, ny))

print(ans if ans > 0 else "TT")

#https://www.acmicpc.net/problem/2667

import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
N = int(input())
queue = deque()
board = []
vis = []
for i in range(N):
    board.append(list(str(sys.stdin.readline().strip())))
    vis.append([0] * N)

complex_num = 0
house = []

for i in range(N):
    for r in range(N):
        if board[i][r] == '0' or vis[i][r] == 1:
            continue
        complex_num += 1
        house_num = 1
        vis[i][r] = 1
        queue.appendleft((i, r))
        while queue:
            x, y = queue.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if board[nx][ny] == '0' or vis[nx][ny] == 1:
                    continue
                house_num += 1
                vis[nx][ny] = 1
                queue.append((nx, ny))
        house.append(house_num)

print(complex_num)
house.sort()
for i in range(len(house)):
    print(house[i])

#https://www.acmicpc.net/problem/5014

import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
elevator = [-1] * (F + 1)
queue = deque()
queue.append(S)
elevator[S] = 0

while queue:
    cur = queue.popleft()
    for next in [cur + U, cur - D]:
        if next <= 0 or next > F:
            continue
        if elevator[next] != -1:
            continue
        elevator[next] = elevator[cur] + 1
        queue.append(next)
print(elevator[G] if elevator[G] >= 0 else "use the stairs")