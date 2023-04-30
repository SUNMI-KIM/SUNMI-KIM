class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = Node(None, self.head, None)
        self.head = Node(None, None, self.tail)
        self.current = None
    
    def add_first(self, data):
        pointer = Node(data, self.head, self.tail)
        self.head.next = pointer
        self.tail.prev = pointer
    
    def add_last(self, data):
        pointer = self.head
        if pointer.next is self.tail:
            self.add_first(data)
        else:
            while pointer.next != self.tail:
                pointer = pointer.next
            pointer.next = Node(data, pointer, self.tail)
            self.tail.prev = pointer.next

    def insert(self, data, index):
        if index == 0:
            self.add_first()
        else:
            pointer = self.head.next
            for i in range(0, index - 1):
                pointer = pointer.next
            pointer.next = Node(data, pointer.prev, pointer.next.next)

    def removefirst(self):
        if self.head != None:
            pointer = self.head.next
            pointer = pointer.next
            pointer.prev = self.head
    
    def removelast(self):
        if self.head.next == None:
            self.removefirst()
        cur_pointer = self.head
        pre_pointer = self.head
        while cur_pointer.next != self.tail:
            pre_pointer = cur_pointer
            cur_pointer = cur_pointer.next
        pre_pointer.next = self.tail
        self.tail.prev = pre_pointer
    
    def remove(self, data):
        if self.head != None:
            if self.head.data == data:
                self.removefirst()
                return True
            pointer = self.head
            while pointer.next != self.tail:
                if pointer.next.data == data:
                    pointer.next = pointer.next.next
                    pointer.next.prev = pointer
                    return True
                pointer = pointer.next
        return False

    def write(self):
        pointer = self.head.next
        while (pointer != self.tail):
            print(pointer.data)
            pointer = pointer.next

