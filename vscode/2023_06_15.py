#https://www.acmicpc.net/problem/2448

N = int(input())
triangle = [[' '] * 2 * N for _ in range(N)]

def solve(x, y, n):
    if n == 3:
        triangle[x][y] = "*"
        triangle[x + 1][y - 1] = "*"
        triangle[x + 1][y + 1] = "*"
        for i in range(-2, 3): 
            triangle[x + 2][y + i] = '*'
        return 0
    n = n // 2
    solve(x, y, n)
    solve(x + n, y - n, n)
    solve(x + n, y + n, n)

solve(0, N-1, N)
for i in range(N):
    print("".join(triangle[i]))