class Node():
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev

class Deque():
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.length = 0
    
    def ft_push_front(self, X):
        if self.length == 0:
            newNode = Node(X, self.head, self.tail)
            self.head.next = newNode
            self.tail.prev = newNode
            self.length += 1
        else:
            newNode = Node(X, self.head, self.head.next)
            self.head.next = newNode
            newNode.next.prev = newNode
            self.length += 1
    
    def ft_push_back(self, X):
        if self.length == 0:
            newNode = Node(X, self.head, self.tail)
            self.head.next = newNode
            self.tail.prev = newNode
            self.length += 1
        else:
            newNode = Node(X, self.tail.prev, self.tail)
            self.tail.prev = newNode
            newNode.prev.next = newNode
            self.length += 1

    def ft_size(self):
        print(self.length)
    
    def ft_empty(self):
        if self.length == 0:
            print(1)
        else:
            print(0)
    
    def ft_front(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.head.next.data)
    
    def ft_back(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.tail.prev.data)

    def ft_pop_front(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.head.next.data)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.length -= 1

    def ft_pop_back(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.tail.prev.data)
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.length -= 1