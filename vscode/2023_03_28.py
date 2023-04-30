#https://www.acmicpc.net/problem/5430
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
        self.current = self.head
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
        return self.length

    def ft_pop_front(self):
        if self.length == 0:
            return 0
        else:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.length -= 1
            return 1

    def ft_pop_back(self):
        if self.length == 0:
            return 0
        else:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.length -= 1
            return 1

T = int(input())
for i in range(0, T):
    deque = Deque()
    p = input()
    n = int(input())
    li = input().replace("[", "").replace(",", " ").replace("]", "").split()
    status = 1

    for r in li:
        deque.ft_push_back(int(r))

    for char in p:
        if char == "R":
            status *= -1
        elif char == "D":
            if status == 1:
                if deque.ft_pop_front() == 0:
                    status = 0
                    break
            else:
                if deque.ft_pop_back() == 0:
                    status = 0
                    break

    if status == 1:
        print("[", end = "")
        for r in range(0, deque.ft_size()):
            deque.current = deque.current.next
            if deque.current.next == deque.tail:
                print(deque.current.data, end = "")
            else:
                print(deque.current.data, end = ",")
        print("]")
    elif status == -1:
        print("[", end = "")
        deque.current = deque.tail
        for r in range(0, deque.ft_size()):
            deque.current = deque.current.prev
            if deque.current.prev == deque.head:
                print(deque.current.data, end = "")
            else:
                print(deque.current.data, end = ",")
        print("]")
    else:
        print("error")