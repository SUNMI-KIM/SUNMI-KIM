#https://www.acmicpc.net/problem/3085
def checkMax(board):
    answer = 1
    for i in range(0, num):
        check = 1
        for r in range(1, num):
            if board[i][r] == board[i][r - 1]:
                check += 1
            else:
                check = 1
            answer = max(check, answer)

        check = 1
        for r in range(1, num):
            if board[r][i] == board[r - 1][i]:
                check += 1
            else:
                check = 1
            answer = max(check, answer)
    return answer

num = int(input())
ans = 1
board = []

for i in range(0, num):
    board.append(list(input()))

for i in range(0, num):
    for r in range(0, num):
        if r + 1 < num:
            board[i][r], board[i][r + 1] = board[i][r + 1], board[i][r]
            cnt = checkMax(board)
            ans = max(cnt, ans)
            board[i][r], board[i][r + 1] = board[i][r + 1], board[i][r]

        if i + 1 < num:
            board[i][r], board[i + 1][r] = board[i + 1][r], board[i][r]
            cnt = checkMax(board)
            ans = max(cnt, ans)
            board[i][r], board[i + 1][r] = board[i + 1][r], board[i][r]
print(ans)

