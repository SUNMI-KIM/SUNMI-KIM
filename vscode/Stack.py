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