
class LinkedList:

    # defines a single node in the linked list
    class Node:
        
        def __init__(self):
            self.value = None
            self.next = None
            
            
    # constructor of the linked list
    def __init__(self):
        self.head = None
        self.back = None
    
    # returns a node with specified value
    def new_node(self, val):
        p = self.Node()
        p.value = val
        return p
        
    # appends a node with the required value to the end of the list
    def append(self, val):
        p = self.new_node(val)
        if self.head == None:
            self.head = p
            self.back = self.head
        else:
            self.back.next = p
            self.back = p
        
    # returns the current size of the list
    def length(self):
        curnode = self.head
        if curnode == None:
            return 0
        counter = 1
        while curnode != self.back:
            curnode = curnode.next
            counter += 1
        return counter
        
    # returns whether the list is empty
    def is_empty(self):
        return not self.head
        
    # returns the value in the list at the current position (0-indexed)
    def get_value(self, pos):
        if self.is_empty():
            return "List is empty"
        if self.length() <= pos:
            return "List has insufficient elements"
        if pos < 0:
            return "Please insert appropriate index" 
        curptr = 0
        curnode = self.head
        while curnode:
            if curptr == pos:
                return curnode.value
            curnode = curnode.next
            curptr += 1
        return None
    
    # inserting element at the beginning of the list
    def insert_at_beginning(self, val):
        if self.head == None:
            self.append(val)
            return
        p = self.new_node(val)
        p.next = self.head
        self.head = p
    
    # inserting element at the specified position in the list (0-indexed)
    def insert_at_position(self, val, pos):
        if pos < 0:
            print("Please insert appropriate index")
            return
        if self.length() < pos:
            print("List has insufficient elements")
            return
        if pos == 0:
            self.insert_at_beginning(val)
            return
        curpos = 0
        curnode = self.head
        while curpos < pos - 1:
            curpos += 1
            curnode = curnode.next
        p = self.new_node(val)
        p.next = curnode.next
        curnode.next = p
        if p.next == None:
            self.back = p
        
    # removing element at the beginning of the list
    def remove_from_beginning(self):
        if self.is_empty():
            return
        if self.length() == 1:
            self.head = None
            self.back = None
            return
        self.head = self.head.next
    
    # removing element at the end of the list
    def remove_from_end(self):
        if self.is_empty():
            return
        if self.length() == 1:
            self.head = None
            self.back = None
            return
        curnode = self.head
        while curnode.next.next:
            curnode = curnode.next
        curnode.next = None
        self.back = curnode
        
    # removing element at a specified position in the list (0-indexed)
    def remove_from_position(self, pos):
        if pos < 0:
            print("Please insert appropriate index")
            return
        if self.length() <= pos:
            print("List has insufficient elements")
            return
        if pos == 0:
            self.remove_from_beginning()
            return
        curpos = 0
        curnode = self.head
        while curpos != pos - 1:
            curpos += 1
            curnode = curnode.next
        if curnode.next == self.back:
            self.remove_from_end()
            return
        curnode.next = curnode.next.next
    
    # reversing the list
    def reverse(self, curnode=None): # doing it recursively, can it be done iteratively??
        if curnode == None:
            if self.head == None: # it means that the list is empty
                return
            else:
                curnode = self.head
        if curnode.next == None: # it means that the list is of size 1
            return
        if curnode.next == self.back:
            curnode.next.next = curnode
            self.head, self.back = self.back, self.head
        else:
            self.reverse(curnode.next)
            curnode.next.next = curnode
        if curnode == self.back:
            curnode.next = None
        
    
    # displaying the list
    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        print("List =", end=" ")
        curnode = self.head
        while curnode:
            print(curnode.value, end=" ")
            curnode = curnode.next
        print()
        
