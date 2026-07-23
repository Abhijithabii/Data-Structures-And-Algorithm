class StackList:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)
        return
    
    def pop(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        self.items.pop()
    def peek(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        """Remove all elements."""
        return self.items.clear()

    def show_stack(self):
        return self.items


stack1= StackList()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.peek())
print(stack1.show_stack())
stack1.pop()
print(stack1.show_stack())
