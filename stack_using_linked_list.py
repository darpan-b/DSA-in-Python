from linked_list import LinkedList

class Stack(LinkedList):
    
    # constructor
    def __init__(self):
        super().__init__()
        self.top = None

    # pushing an element onto the stack
    def push(self, val):
        self.append(val)
        self.top = self.back
    
    # popping an element from the stack
    def pop(self):
        if not self.is_empty():
            self.remove_from_end()
            self.top = self.back
    
    # returning the top element on the stack
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.value
            

def main():
    S = Stack()
    S.push(27)
    print(S.peek())
    S.push(32)
    S.push(29)
    S.push(7)
    print(S.peek())
    print(S.length())
    S.pop()
    print(S.peek())
    S.pop()
    print(S.peek())
    S.pop()
    print(S.peek())
    S.pop()
    print(S.peek())
    S.push(16)
    print(S.peek(), S.length())
    S.push(2)
    print(S.peek(), S.length())

if __name__ == "__main__":
    main()
