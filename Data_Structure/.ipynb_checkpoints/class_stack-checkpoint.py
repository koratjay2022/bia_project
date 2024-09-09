class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value) 
        print(f"{value} pushed value")

    def pop(self):
        if self.is_empty():  
            print("Stack Underflow")
            return None
        else:
            value = self.stack.pop()  
            print(f"{value} popped value.")
            return value

    def peek(self):
        if self.is_empty():
            print("Empty!")
            return None
        else:
            print(f"Top element is {self.stack[-1]}")
            return self.stack[-1]  

    def is_empty(self):
        return len(self.stack) == 0 

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements:", self.stack)