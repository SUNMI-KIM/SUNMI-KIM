#https://www.acmicpc.net/problem/1904
a = int(input())
cur, next = 1, 2
sum = 0
if a == 1:
    print(a)
elif a == 2:
    print(a)
else:
    for i in range(2, a):
        sum = (cur + next) % 15746
        cur, next = next, sum
    print(sum)