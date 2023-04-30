#https://www.acmicpc.net/problem/1003
a = int(input())

for i in range(0, a):
    b = int(input())
    count0 = {0:1, 1:0}
    count1 = {0:0, 1:1}
    r = 2
    while r < b+1:
        count0[r] = count0[r-1] + count0[r-2]
        count1[r] = count1[r-1] + count1[r-2]
        r += 1
    print(count0[b], count1[b])

