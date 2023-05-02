#https://www.acmicpc.net/problem/2824
import sys

def GCD(a, b):
    while (b > 0):
        tmp = a
        a = b
        b = tmp % b
    return a

N = int(input())
A = 1
array = list(map(int, sys.stdin.readline().split()))
for i in array:
    A *= i

M = int(input())
B = 1
array = list(map(int, sys.stdin.readline().split()))
for i in array:
    B *= i

print('%s' %str(GCD(A, B))[-9:])

#https://www.acmicpc.net/problem/6588
import sys

sifter = [1] * (1000000)
primeNum = []
for i in range(2, 1000000):
    if sifter[i] == 1:
        primeNum.append(i)
        for r in range(i + i, 1000000, i):
            sifter[r] = 0
            
def binarySearch(target):
    start = 0
    end = len(primeNum) - 1
    while (start <= end):
        mid = (start + end) // 2
        if primeNum[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end

def linearSearch(N, scope):  
    for i in range(1, scope + 1):
        for r in range(scope, i - 1, -1):
            if (primeNum[i] + primeNum[r] == N):
                return print("%d = %d + %d" %(n, primeNum[i], primeNum[r]))
            elif (primeNum[i] + primeNum[r] < N):
                break

while (1):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    linearSearch(n, binarySearch(n))
    
#https://www.acmicpc.net/problem/1644
import sys

def sieveEratosthenes(N):
    sifter = [1] * (N + 1)
    primeNum = []
    for i in range(2, N + 1):
        if sifter[i] == 1: 
            primeNum.append(i)
            for r in range(i + i, N + 1, i):
                sifter[r] = 0
    return primeNum

N = int(sys.stdin.readline())
primeRange = sieveEratosthenes(N)

start = 0
end = 0
numberCase = 0
sumPrime = 0

while (end < len(primeRange) or sumPrime >= N):
    if sumPrime < N:
        if end < len(primeRange):
            sumPrime += primeRange[end]
            end += 1
        else:
            break
    else:
        sumPrime -= primeRange[start]
        start += 1
    if sumPrime == N:
        numberCase += 1

print(numberCase)