#https://www.acmicpc.net/problem/18111
import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = []
for i in range(N):
    ground.extend(list(map(int, sys.stdin.readline().split())))

min_time = float('inf')
max_block = 0

for target_height in range(0, 257):
    time = 0
    block_needed = 0
    block_save = 0
    for height in ground:
        if height > target_height:
            time += (height - target_height) * 2
            block_save += height - target_height 
        elif height < target_height:
            time += target_height - height
            block_needed += target_height - height
    if block_save + B < block_needed:
        continue
    if time < min_time:
        min_time = time
        max_block = target_height
    elif time == min_time:
        max_block = max(target_height, max_block)
print(min_time, max_block)

#https://www.acmicpc.net/problem/11723
class Set():
    def __init__(self):
        self.s = {}
        for i in range(1, 21):
            self.s[i] = False
    
    def ft_add(self, x):
        self.s[x] = True
    
    def ft_remove(self, x):
        self.s[x] = False
    
    def ft_check(self, x):
        if self.s[x]:
            print(1)
        else:
            print(0)
    
    def ft_toggle(self, x):
        if self.s[x]:
            self.s[x] = False
        else:
            self.s[x] = True
    
    def ft_all(self):
        for i in range(1, 21):
            self.s[i] = True
        
    def ft_empty(self):
        for i in range(1, 21):
            self.s[i] = False

import sys

M = int(input())

s = Set()
for i in range(0, M):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == "add":
        s.ft_add(int(command[1]))
    elif command[0] == "check":
        s.ft_check(int(command[1]))
    elif command[0] == "remove":
        s.ft_remove(int(command[1]))
    elif command[0] == "toggle":
        s.ft_toggle(int(command[1]))
    elif command[0] == "all":
        s.ft_all()
    elif command[0] == "empty":
        s.ft_empty()

#https://www.acmicpc.net/problem/11399
import sys

N = int(input())
time = list(map(int, sys.stdin.readline().split()))
time.sort()

min_time = 0
for i in range(len(time)):
    min_time += time[i] * (len(time) - i)
print(min_time)

#https://www.acmicpc.net/problem/17219
import sys

N, M = map(int, sys.stdin.readline().split())
passwords = {}
for i in range(N):
    site, password = map(str, sys.stdin.readline().strip().split())
    passwords[site] = password

for i in range(M):
    site = sys.stdin.readline().strip()
    print(passwords[site])