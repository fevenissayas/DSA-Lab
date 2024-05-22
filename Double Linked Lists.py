class Node:
    def __innit__ (self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append (self, value):
        new_node = Node (value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    
    def prepend (self, value):
        new_node = Node (value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def delete (self, value):
        #input_value = Node (value)
        search_element = self.head
        if value == search_element:
            self.head = self.head.next
            return
        if value == self.tail:
            self.tail = self.tail.prev
        
        while search_element:
            if value == search_element:
                if search_element.prev:
                    search_element.prev.next = search_element.next
                else:
                    self.head = search_element.next
                if search_element.next:
                    search_element.next.prev = search_element.prev
                if search_element == self.tail:
                    self.tail = search_element.prev
                return
            search_element = search_element.next
