#https://www.acmicpc.net/problem/1614
finNum = int(input())
num = int(input())
if finNum == 5:
    print(num * 8 + finNum - 1)
elif finNum == 1:
    print(num * 8)
elif num % 2 != 0:
    print(num * 4 + 5 - finNum)
elif num % 2 == 0:
    print(num * 4 + finNum - 1)

#stack
#https://www.acmicpc.net/problem/1935
num = int(input())
dic = {}
stack = []
ex = input()

for i in range(0, num):
    dic[chr(ord("A") + i)] = int(input())

for s in ex:
    if s not in dic:
        one = stack.pop()
        two = stack.pop()
        if s == "+":
            stack.append(two + one)
        elif s == "-":
            stack.append(two - one)
        elif s == "/":
            stack.append(two / one)
        elif s == "*":
            stack.append(two * one)
    else:
        stack.append(dic[s])
print("{:.2f}".format(stack.pop()))

#stack
#https://www.acmicpc.net/problem/2504
dic = {"H" : 1, "C" : 12, "O" : 16}
num = 0

index = 0
stackIndex = []
stack = []

chemical = input()
for c in chemical:
    if c.isalpha():
        stack.append(dic[c])
        index += 1
    elif c == "(":
        stackIndex.append(index)
    elif c == ")":
        index = stackIndex.pop()
        while len(stack) > index:
            num += stack.pop()
        stack.append(num)
        num = 0
        index += 1
    elif c.isdigit():
        stack.append(stack.pop() * int(c))
print(sum(stack))


