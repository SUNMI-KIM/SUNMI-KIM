import sys
a = int(input())
b = sorted(list(map(int, sys.stdin.readline().split())))
c = int(input())

idx_left = 0
idx_right = len(b)-1
count = 0
while (idx_left < idx_right):
    if b[idx_left] + b[idx_right] == c:
        idx_left += 1
        idx_right -= 1
        count += 1
    elif b[idx_left] + b[idx_right] < c:
        idx_left += 1
    else:
        idx_right -= 1
print(count)