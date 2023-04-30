#https://www.acmicpc.net/problem/1021
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
search = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, N + 1)])
ans = 0

for i in search:
    if (queue.index(i) < len(queue) / 2):
        while (queue[0] != i):
            queue.rotate(-1)
            ans += 1
            
    else:
        while (queue[0] != i):
            queue.rotate(1)
            ans += 1
    queue.popleft()

print(ans)