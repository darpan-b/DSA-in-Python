from linked_list import LinkedList

class Queue(LinkedList):
    
    # constructor
    def __init__(self):
        super().__init__()
        self.front = None
        self.rear = None

    # pushing an element onto the stack
    def push(self, val):
        self.append(val)
        if self.front == None:
            self.front = self.head
        self.rear = self.back
    
    # popping an element from the stack
    def pop(self):
        if self.is_empty():
            return
        self.remove_from_beginning()
        if self.head == None:
            self.front = None
            self.rear = None
        else:
            self.front = self.head
    
    # returning the top element on the stack
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.value
            

def main():
    Q = Queue()
    Q.push(27)
    print(Q.peek())
    Q.push(32)
    Q.push(29)
    Q.push(7)
    print(Q.peek())
    print(Q.length())
    Q.pop()
    print(Q.peek())
    Q.pop()
    print(Q.peek())
    Q.pop()
    print(Q.peek())
    Q.pop()
    print(Q.peek())
    Q.push(16)
    print(Q.peek(), Q.length())
    Q.push(2)
    print(Q.peek(), Q.length())

if __name__ == "__main__":
    main()

