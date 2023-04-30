class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None)
    
    def add_first(self, data):
        if self.head.next == None:
            pointer = self.head
            newNode = Node(data, None)
            self.head.next = newNode
            newNode.next = newNode
        else:
            newNode = Node(data, None)
            newNode.next = self.head.next
            self.head.next = newNode
            pointer = newNode.next
            while (pointer.next != newNode.next):
                pointer = pointer.next
            pointer.next = newNode
        
    def add_last(self, data):
        pointer = self.head
        if pointer.next is None:
            self.add_first(data)
        else:
            first_pointer = self.head.next
            cur_pointer = self.head.next    
            while cur_pointer.next != first_pointer:
                cur_pointer = cur_pointer.next
            cur_pointer.next = Node(data, first_pointer)

    def insert(self, data, index):
        if index == 0:
            self.add_first()
        else:
            pointer = self.head.next
            for i in range(0, index - 1):
                pointer = pointer.next
            pointer.next = Node(data, pointer.next)

    def removefirst(self):
        if self.head.next != None:
            first_pointer = self.head.next
            last_pointer = self.head.next
            while last_pointer.next != first_pointer:
                last_pointer = last_pointer.next
            last_pointer.next = first_pointer.next
            self.head.next = first_pointer.next
    
    def removelast(self):
        if self.head.next == None:
            self.removefirst()
        else:
            pre_pointer = self.head.next
            cur_pointer = self.head.next
            first_pointer = self.head.next
            while cur_pointer.next != first_pointer:
                pre_pointer = cur_pointer
                cur_pointer = cur_pointer.next
            pre_pointer.next = first_pointer
    
    def remove(self, data):
        if self.head.next != None:
            if self.head.next.data == data:
                self.removefirst()
                return True
            pointer = self.head.next
            first_pointer = self.head.next
            while pointer.next != first_pointer:
                if pointer.next.data == data:
                    pointer.next = pointer.next.next
                    return True
                pointer = pointer.next
        return False

    def write(self):
        pointer = self.head.next
        print(pointer.data, end = " ")
        pointer = pointer.next
        while (pointer != self.head.next):
            print(pointer.data, end = " ")
            pointer = pointer.next


