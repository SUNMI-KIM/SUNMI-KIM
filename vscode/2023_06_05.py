#https://www.acmicpc.net/problem/2577
A = int(input())
B = int(input())
C = int(input())
dic = {}

for i in range(10):
    dic[i] = 0

abc = A * B * C
while abc > 0:
    dic[abc % 10] += 1
    abc //= 10

for i in dic.values():
    print(i)

#https://www.acmicpc.net/problem/1926
import queue
import sys

class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

Queue = queue.Queue()
n, m = map(int, sys.stdin.readline().split())
board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
vis = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    vis.append([0] * m)

art_num = 0
max_area = 0
for i in range(n):
    for r in range(m):
        if vis[i][r] or board[i][r] == 0:
            continue
        art_num += 1
        vis[i][r] = 1
        Queue.put(Pair(i, r))
        area = 0
        while(Queue.empty() == False):
            area += 1
            cur = Queue.get()
            for dir in range(0, 4):
                nx = cur.x + dx[dir]
                ny = cur.y + dy[dir]
                if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                    continue
                if (vis[nx][ny] or board[nx][ny] != 1):
                    continue
                vis[nx][ny] = 1
                Queue.put(Pair(nx, ny))
        max_area = max(max_area, area)
print(art_num)
print(max_area)

#https://www.acmicpc.net/problem/2178

import queue
import sys

class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

Queue = queue.Queue()
n, m = map(int, sys.stdin.readline().split())
board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = []
for i in range(n):
    board.append(list(str(sys.stdin.readline().strip())))
    dist.append([-1] * m)

Queue.put(Pair(0, 0))
dist[0][0] = 0
while(Queue.empty() == False):
    cur = Queue.get()
    for dir in range(0, 4):
        nx = cur.x + dx[dir]
        ny = cur.y + dy[dir]
        if (nx < 0 or nx >= n or ny < 0 or ny >= m):
            continue
        if (dist[nx][ny] >= 0 or board[nx][ny] != '1'):
            continue
        dist[nx][ny] = dist[cur.x][cur.y] + 1
        Queue.put(Pair(nx, ny))
print(dist[n - 1][m - 1] + 1)