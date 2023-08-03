#https://www.acmicpc.net/problem/2661

def check(c, addstr):
    temp = "".join(c) + addstr
    for i in range(1, len(temp) // 2 + 1):
        if temp[-2 * i : -1 * i] == temp[-1 * i :]:
            return False
    return True

def solve(c):
    if len(c) == N:
        print("".join(c))
        exit() 

    for char in ["1", "2", "3"]:
        if check(c, char):
            c.append(char)
            solve(c)
            c.pop()


N = int(input())
solve(["1"])
