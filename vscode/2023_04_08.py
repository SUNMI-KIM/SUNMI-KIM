#https://www.acmicpc.net/problem/11726
n = int(input())
rectangle = [0] * (n + 2)
rectangle[1], rectangle[2] = 1, 2

for i in range(3, n + 1):
    rectangle[i] = rectangle[i - 1] + rectangle[i - 2]
print(rectangle[n] % 10007)