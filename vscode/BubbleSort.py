import random

N = int(input())
arr = []
for i in range(N):
    arr.append(random.randrange(1, N))

print(arr)

for i in range(N):
    for r in range(1, N - i):
        if arr[r] < arr[r - 1]:
            arr[r], arr[r - 1] = arr[r - 1], arr[r]

print(arr)