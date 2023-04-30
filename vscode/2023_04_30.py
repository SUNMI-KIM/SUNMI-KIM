#https://www.acmicpc.net/problem/2004
import sys

def count_factor(n, factor):
    count = 0
    div = factor
    while n >= div:
        count += n // div
        div *= factor
    return count

n, m = map(int, sys.stdin.readline().split())
print(min(count_factor(n, 2) - count_factor(m, 2) - count_factor(n-m, 2),
          count_factor(n, 5) - count_factor(m, 5) - count_factor(n-m, 5)))