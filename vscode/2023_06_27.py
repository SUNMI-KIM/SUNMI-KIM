#https://www.acmicpc.net/problem/1182

import sys

N, S = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
arr = [1000001] * (N + 1)
ans = 0

def solve(num, sum):
    if num >= N:
        return
    sum += sequence[num]
    if sum == S:
        global ans
        ans += 1
    
    solve(num + 1, sum)
    solve(num + 1, sum - sequence[num])
    
            
solve(0, 0)
print(ans)

#https://www.acmicpc.net/problem/6603

import sys

def solve(cnt, cur):
    if cnt == 7:
        for i in range(1, 7):
            print(arr[i], end = " ")
        print()
        return
    for i in range(cur, len(S)):
        arr[cnt] = S[i]
        solve(cnt + 1, i + 1)

while True:
    S = list(map(int, sys.stdin.readline().split()))
    arr = [0] * 7
    if len(S) == 1:
        break
    solve(1, 1) 
    print()

#https://www.acmicpc.net/problem/1759

import sys

L, C = map(int, sys.stdin.readline().split())
alphabet = sorted(list(map(str, sys.stdin.readline().split())))
dic = {"a" : 1, "e" : 1, "i" : 1, "o" : 1, "u" : 1}
stack = [0] * 20
isused = [0] * 20

def check():
    gather = 0
    consonant = L
    for i in range(L):
        if stack[i] in dic:
            gather += 1
            consonant -= 1
    
    if gather > 0 and consonant > 1:
        return True
    return False

def solve(idx, cnt):
    if cnt == L:
        if not check():
            return 
        for i in range(0, L):
            print(stack[i], end="")
        print()
        return

    for i in range(idx, C):
        if not isused[i]:
            isused[i] = 1
            stack[cnt] = alphabet[i]
            solve(i + 1, cnt + 1)
            isused[i] = 0

solve(0, 0)
