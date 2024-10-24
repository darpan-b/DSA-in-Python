class DoublyLinkedList:

    # defines a single node in the linked list
    class Node:
        def __init__(self):
            self.value = None
            self.prev = None
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
            p.prev = self.back
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
        self.head.prev = p
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
        p.prev = curnode
        curnode.next = p
        if p.next == None:
            self.back = p
        else:
            p.next.prev = p
        
    # removing element at the beginning of the list
    def remove_from_beginning(self):
        if self.is_empty():
            return
        if self.length() == 1:
            self.head = None
            self.back = None
            return
        self.head = self.head.next
        self.head.prev = None
    
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
        curnode.next.next.prev = curnode
        curnode.next = curnode.next.next
    
    # reversing the list
    def reverse(self):
        curnode = self.head
        while curnode:
            curnode.next, curnode.prev = curnode.prev, curnode.next
            curnode = curnode.prev
        self.head, self.back = self.back, self.head
    
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
        

def main():
    L = DoublyLinkedList()
    print(L.length())
    print(L.is_empty())
    L.append(10)
    print(L.length())
    print(L.head.value, L.back.value)
    L.append(15)
    L.append(32)
    print(L.head.value, L.back.value)
    print(L.length())
    L.remove_from_beginning()
    L.display()
    L.remove_from_end()
    L.display()
    L.append(36)
    L.append(107)
    L.append(76)
    L.display()
    L.remove_from_position(2)
    L.display()
    L.remove_from_position(6)
    L.display()
    L.remove_from_position(-1)
    L.display()
    L.insert_at_beginning(92)
    L.display()
    L.append(69)
    L.display()
    L.insert_at_position(20, 1)
    L.display()
    L.insert_at_position(502, 0)
    L.display()
    L.insert_at_position(78, 7)
    L.display()
    L.insert_at_position(17, -6)
    L.insert_at_position(-10, 10)
    L.display()
    print(L.head.value, L.back.value)
    L.remove_from_position(0)
    L.display()
    print(L.head.value, L.back.value)
    L.remove_from_position(6)
    L.display()
    print(L.head.value, L.back.value)
    L.reverse()
    L.display()
    print(L.head.value, L.back.value)
    L2 = DoublyLinkedList()
    L2.reverse()
    L2.display()
    L2.append(26)
    L2.reverse()
    L2.display()
    print(L2.length())
    L2.append(10)
    L2.display()
    print(L2.head.prev, L2.head.next.value, L2.back.prev.value, L2.back.next)
    L2.reverse()
    L2.display()
    

if __name__ == "__main__":
    main()


