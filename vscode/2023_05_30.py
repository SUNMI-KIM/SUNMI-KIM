#https://www.acmicpc.net/problem/5525
import sys

N = int(input())
S_length = int(input())
S = sys.stdin.readline().strip()
result = 0

for i in range(S_length - (2 * N + 1)):
    index = 0
    while (index <= 2 * N + 1):
        if S[index + i] != "I":
            break
        index += 1
        if index == 2 * N + 1:
            result += 1
            break
        if S[index + i] != "O" or index == 2 * N + 2:
            break
        index += 1
print(result)

#https://www.acmicpc.net/problem/1107
import sys

N = int(input())
M = int(input())
button = {0 : True, 1 : True, 2 : True, 3 : True, 4 : True,
           5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
if M > 0:
    broken_button = list(map(int, sys.stdin.readline().split()))
    for i in broken_button:
        button[i] = False

number = float("inf")
sunmi = 0
for i in range(0, 1000000):
    index = 0
    for r in str(i):
        if button[int(r)] == False:
            break
        else:
            index += 1
    if index == len(str(i)):
        number = min(number, abs(N - i) + len(str(i)))
number = min(number, abs(N - 100))
print(number)