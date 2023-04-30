#https://www.acmicpc.net/problem/10448
N = int(input())

li = []
ans = []
for i in range(1, 46):
    li.append(int(i * (i + 1) / 2))

for i in li:
    for r in li:
        for l in li:
            if i + r + l <= 1000:
                ans.append(i + r + l)
            else:
                break

for i in range(0, N):
    K = int(input())
    print(int(K in ans))

