class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def reverseList(self, value):
        value = Node (value)
        node = None
        iterator = self.head
        while iterator.next:
            temp = iterator
            self.head = iterator.next
            