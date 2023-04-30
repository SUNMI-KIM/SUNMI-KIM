class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def search(self, data):
        index = 0
        pointer = self.head
        while pointer != None:
            if pointer.data == data:
                return index
            index += 1
            pointer = pointer.next
        return -1
    
    def add_first(self, data):
        pointer = self.head
        self.head = Node(data, pointer)
    
    def add_last(self, data):
        pointer = self.head
        if pointer is None:
            self.add_first(data)
        else:    
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = Node(data, None)

    def insert(self, data, index):
        if index == 0:
            self.add_first()
        else:
            pointer = self.head
            for i in range(0, index - 1):
                pointer = pointer.next
            pointer.next = Node(data, pointer.next)

    def removefirst(self):
        if self.head != None:
            self.head = self.head.next
    
    def removelast(self):
        if self.head.next == None:
            self.removefirst()
        cur_pointer = self.head
        pre_pointer = self.head
        while cur_pointer.next != None:
            pre_pointer = cur_pointer
            cur_pointer = cur_pointer.next
        pre_pointer.next = None
    
    def remove(self, data):
        if self.head != None:
            if self.head.data == data:
                self.removefirst()
                return True
            pointer = self.head
            while pointer.next != None:
                if pointer.next.data == data:
                    pointer.next = pointer.next.next
                    return True
                pointer = pointer.next
        return False

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

ll = SinglyLinkedList()

ll.add_last("a")
ll.add_last("b")
ll.add_first("t")
ll.add_last("c")
ll.add_last("d")
ll.insert("f", 4)
for item in ll:
    print(item)

