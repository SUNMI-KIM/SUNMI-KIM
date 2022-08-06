#https://www.acmicpc.net/problem/1764
dic = {}
li = []
a = input().split()
b = int(a[0]) + int(a[1])
for i in range(0, b):
    c = input()
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] = 2
for key, value in dic.items():
    if value == 2:
        li.append(key)
li = sorted(li)
print(len(li))
for i in range(0, len(li)):
    print(li[i])

#https://www.acmicpc.net/status?user_id=hariaus&problem_id=10816&from_mine=1
def binary_search(target, list, start, end):
    if start > end :
        return 0
    
    mid = (start + end) // 2
    if list[mid] == target:
        return list[start:end+1].count(target)
    if list[mid] > target:
        return binary_search(target, list, start, mid - 1)
    else:
        return binary_search(target, list, mid + 1, end)

a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))
b = sorted(b)
dic = {}
for n in b:
    if n not in dic:
        dic[n] = binary_search(n, b, 0, len(b) - 1)
li = []
for n in d:
    if n in dic:
        li.append("%d" %(dic[n]))
    else:
        li.append("0")
print(" ".join(li))


   