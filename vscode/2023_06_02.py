#https://www.acmicpc.net/problem/2504
#리팩토링 하기
class Stack():
    def __init__(self):
        self.stack = []
        self.length = 0

    def ft_pop(self):
        if self.length < 1:
            return -1
        else:
            self.length -= 1
            return self.stack.pop()

    def ft_push(self, data):
        self.stack.append(data)
        self.length += 1

    def ft_size(self):
        return self.length

    def ft_empty(self):
        if self.length < 1:
            return True
        else:
            return False

    def ft_top(self):
        if self.length < 1:
            return "no"
        else:
            return self.stack[self.length - 1]

import sys

stack = Stack()
string = sys.stdin.readline().strip()
bracket = {")": 2, "]": 3}
open_close = {"]": "[", ")": "("}
flag = 0
ans = 0

for s in string:
    if s == "(" or s == "[":
        stack.ft_push(s)
    elif s == "]" or s == ")":
        if stack.ft_empty():
            flag = 1
            break
        elif str(stack.ft_top()).isdigit():
            tmp = 0
            while stack.ft_top() != open_close[s]:
                if stack.ft_empty():
                    flag = 1
                    break
                top = stack.ft_pop()
                if isinstance(top, int):  # 숫자로 변환된 경우만 계산
                    tmp += top * bracket[s]
                else:  # 괄호 문자열인 경우
                    flag = 1
                    break
            if flag:
                break
            stack.ft_pop()
            stack.ft_push(tmp)
        else:
            if stack.ft_top() != open_close[s]:
                flag = 1
                break
            stack.ft_pop()
            stack.ft_push(bracket[s])

while not stack.ft_empty() and flag != 1:
    top = stack.ft_pop()
    if isinstance(top, int):  # 숫자인 경우만 합산
        ans += top
    else:  # 괄호 문자열인 경우
        flag = 1
        break

if flag == 1 or not stack.ft_empty():
    ans = 0

print(ans)

#https://www.acmicpc.net/problem/10808
from string import ascii_lowercase

alphabet = {}
for i in ascii_lowercase:
    alphabet[i] = 0

S = input()
for s in S:
    alphabet[s] += 1

for num in alphabet.values():
    print(num, end = " ")