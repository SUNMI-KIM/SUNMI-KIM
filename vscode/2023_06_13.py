#https://www.acmicpc.net/problem/11729
def func(a, b, n): #원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법을 출력하는 함수
    if n == 1:
        return print(a, b)
    func(a, 6 - a - b, n - 1)
    print(a, b)
    func(6 - a - b, b, n - 1)

N = int(input())
print(2 ** N - 1)
func(1, 3, N)

#https://www.acmicpc.net/problem/1074
import sys

def func(n, r, c):
    if n == 0: return 0
    half = 2 ** (n - 1)
    if r < half and c < half: # 1사분면
        return func(n - 1, r, c)
    elif r < half and c >= half: # 2사분면
        return half * half + func(n - 1, r, c - half)
    elif r >= half and c < half: # 3사분면
        return 2 * half * half + func(n - 1, r - half, c)
    return 3 * half * half + func(n - 1, r - half, c - half) # 4사분면

N, r, c = map(int, sys.stdin.readline().split())
print(func(N, r, c))


#https://www.acmicpc.net/problem/17478
N = int(input())

def _bar(str, stk):
    for i in range(stk):
        print("____" , end = "")
    print(str)

def solve(n):
    _bar("\"재귀함수가 뭔가요?\"", n)
    if n == N:
        _bar("\"재귀함수는 자기 자신을 호출하는 함수라네\"", n)
    else:
        _bar("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.", n)
        _bar("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.", n)
        _bar("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"", n)
        solve(n + 1)
    _bar("라고 답변하였지.", n)

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
solve(0)

#https://www.acmicpc.net/problem/1780
import sys

paper = []
num = {-1 : 0, 0 : 0, 1 : 0}

def check(x, y, n):
    for i in range(x, x + n):
        for r in range(y, y + n):
            if paper[x][y] != paper[i][r]:
                return False
    return True

def solve(x, y, n):
    if check(x, y, n):
        num[paper[x][y]] += 1
        return 
    n = n // 3
    for i in range(3):
        for r in range(3):
            solve(x + i * n, y + r * n, n)

N = int(input())
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

solve(0, 0, N)
for i in num.values():
    print(i)

#https://www.acmicpc.net/problem/2630
import sys

paper = []
num = {0 : 0, 1 : 0}

def check(x, y, n):
    for i in range(x, x + n):
        for r in range(y, y + n):
            if paper[x][y] != paper[i][r]:
                return False
    return True

def solve(x, y, n):
    if check(x, y, n):
        num[paper[x][y]] += 1
        return
    n = n // 2
    for i in range(0, 2):
        for r in range(0, 2):
            solve(x + i * n, y + r * n, n)

N = int(input())
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

solve(0, 0, N)
for i in num.values():
    print(i)

#https://www.acmicpc.net/problem/1992

import sys

video = []

def check(x, y, n):
    for i in range(x, x + n):
        for r in range(y, y + n):
            if video[x][y] != video[i][r]:
                return False
    return True

def solve(x, y, n):
    if check(x, y, n):
        print(video[x][y], end="")
        return
    print("(", end="")
    n = n // 2
    for i in range(2):
        for r in range(2):
            solve(x + i * n, y + r * n, n)
    print(")", end="")

N = int(input())
for i in range(N):
    video.append(list(str(sys.stdin.readline().strip())))

solve(0, 0, N)

#https://www.acmicpc.net/problem/2447

star = []

def solve(x, y, n):
    if n == 3:
        for i in range(x, x + 3):
            for r in range(y, y + 3):
                if i != x + 1 or r != y + 1:
                    star[i][r] = "*"
        return
    n = n // 3
    for i in range(3):
        for r in range(3):
            if i == 1 and r == 1:
                continue
            solve(x + i * n, y + r * n, n)

N = int(input())
for i in range(N):
    star.append([" "] * N)

solve(0, 0, N)
for i in range(N):
    print("".join(star[i]))