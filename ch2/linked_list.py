# Linked list
# basic implementation

class Node:
    __slots__ = ["next", "data"]

    def __init__(self, data):
        self.next = None
        self.data = data
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            end = Node(data)
            n = self.head
            while(n.next != None):
                n = n.next
            n.next = end
    def __len__(self):
        if self.head == None:
            return 0
        count = 1
        n = self.head
        while(n.next != None):
            count += 1
            n = n.next
        return count
    def __str__(self):
        s = "["
        if self.head == None:
            return "Empty list"
        n = self.head
        while(n.next != None):
            s += str(n.data) + ", "
            n = n.next
        s += str(n.data) + "]"
        return s
