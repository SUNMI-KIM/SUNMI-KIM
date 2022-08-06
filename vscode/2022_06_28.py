#https://www.acmicpc.net/problem/1205
import sys
num, my_score, capacity = map(int, sys.stdin.readline().split())
if num == 0:   
    print(1)
else:
    li = list(map(int, sys.stdin.readline().split()))
    if num < capacity:
        for r in range(0, capacity-num):
            li.append(-1)
    dic = {}
    for i in range(0, capacity):
        if li[i] not in dic:
            dic[li[i]] = i+1

    for i in range(0, len(li)):
        if li[i] < my_score:
            if my_score in dic:
                print(dic[my_score])
                break
            else:
                print(i+1)
                break
        if i == len(li) - 1:
            print(-1)
