#https://www.acmicpc.net/problem/2960
import sys

def solution(N, K):
    primeNumber = [1] * (N + 1)

    for i in range(2, N + 1):
        if primeNumber[i] == 1:
            for r in range(i, N + 1, i):
                if primeNumber[r] == 1:
                    primeNumber[r] = 0
                    K -= 1
                    if K == 0:
                        return r
                    
N, K = map(int, sys.stdin.readline().split())
print(solution(N, K))

#https://www.acmicpc.net/problem/4948
import sys

def solution(N):
    primeNumber = [1] * (N + 1)
    primeNumber[0], primeNumber[1] = 0, 0

    for i in range(2, N + 1):
        if primeNumber[i] == 1:
            for r in range(i, N + 1, i):
                if primeNumber[r] == 1 and r != i:
                    primeNumber[r] = 0
    
    return sum(primeNumber)

while (1):
    n = int(input())
    if n == 0:
        break
    print(solution(n * 2) - solution(n))     