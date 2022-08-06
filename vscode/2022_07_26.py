import sys
import math

def tof(a):
    for r in range(3, int(math.sqrt(a))+1):
        if a % r == 0:
            return False
    return True


a, b = map(int, sys.stdin.readline().split())
li = []
for i in range(a, b+1):
    if i == 1:
        continue
    elif i == 2:
        li.append(str(i))
    elif i % 2 == 0:
        continue
    elif tof(i) == True:
        li.append(str(i))
print("\n".join(li))