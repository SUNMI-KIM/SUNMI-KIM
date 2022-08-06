#https://www.acmicpc.net/problem/1920
import sys
a = int(input())
b = sorted(list(map(str, sys.stdin.readline().split())))
c = int(input())
d = list(map(str, sys.stdin.readline().split()))

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if element == some_list[mid_index]:
            return 1

        elif element < some_list[mid_index]:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    return 0
for i in range(c):
    print(binary_search(d[i], b))

#https://www.acmicpc.net/problem/2003
import sys
a, b= map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
now_id = 0
last_id = now_id
result = 0
p_r = 0
while(now_id < a):
    if last_id >= a:
        break
    result += c[last_id]
    if result == b:
        p_r += 1
        now_id += 1
        last_id = now_id
        result = 0
    elif result > b:
        now_id += 1
        last_id = now_id
        result = 0
    elif result < b:
        last_id += 1
print(p_r)

#https://www.acmicpc.net/problem/1427
a = input()
li = []
for i in range(0, len(a)):
    li.append(a[i])
li = sorted(li, reverse=True)
for i in li:
    print(i, end="")
