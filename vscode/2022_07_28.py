#https://www.acmicpc.net/problem/1620
import sys
a, b = map(int, sys.stdin.readline().split())
str_dic = {}
int_dic = {}
for i in range(a):
    c = input()
    str_dic[c] = i+1
    int_dic[i+1] = c
for i in range(b):
    d = input()
    if d.isdigit():
        print(int_dic[int(d)])
    else:
        print(str_dic[d])