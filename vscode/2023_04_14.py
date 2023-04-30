#https://www.acmicpc.net/problem/1918
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
            return -1
        else:
            return self.stack[self.length - 1]
        
    def write(self):
        while (self.ft_top() != -1):
            print(self.ft_pop(), end = "")

def compare(top, N):
    dic = {"*" : 2, "/" : 2, "+" : 1, "-" : 1, "(" : 3}
    return dic[N] - dic[top]

expression = list(str(input()))
flag = 0
stack = Stack()
for i in range(len(expression)):
    if expression[i].isalpha():
        print(expression[i] , end = "")
    elif expression[i] == ")":
        while (stack.ft_top() != "("):
            print(stack.ft_pop(), end = "")
        stack.ft_pop()
    elif stack.ft_empty():
        stack.ft_push(expression[i])
    elif expression[i] == '(':
        stack.ft_push(expression[i])
    elif compare(stack.ft_top(), expression[i]) > 0:
        stack.ft_push(expression[i])
    elif compare(stack.ft_top(), expression[i]) == 0:
        print(stack.ft_pop(), end = "")
        stack.ft_push(expression[i])
    elif compare(stack.ft_top(), expression[i]) < 0:
        while (stack.ft_empty() != True):
            if (stack.ft_top() == "("):
                break
            print(stack.ft_pop(), end = "")
        stack.ft_push(expression[i])
stack.write()