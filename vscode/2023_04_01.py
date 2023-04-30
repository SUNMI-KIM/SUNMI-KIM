#https://www.acmicpc.net/problem/2309
li = []
one = 0
two = 0
for i in range(0, 9):
    li.append(int(input()))

for i in range(0, 9):
    for r in range(i + 1, 9):
        if (sum(li) - (li[i] + li[r])) == 100:
            one = li[i]
            two = li[r]
            break

li.remove(one)
li.remove(two)
li.sort()
for i in li:
    print(i)

#https://www.acmicpc.net/problem/2231
N = input()
ans = 0
flag = 0

for i in range(0, int(N)):
    ans = i
    for r in str(i):
        ans += int(r)
    if ans == int(N):
        flag = 1
        ans = i
        break
if flag == 0:
    print(0)
else:
    print(ans)
