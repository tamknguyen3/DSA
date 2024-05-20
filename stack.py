class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2

    # Peek at the top item without removing it
    print(stack.peek())  # Output: 1

    # Get the size of the stack
    print(stack.size())  # Output: 1

    # Check if the stack is empty
    print(stack.is_empty())  # Output: False
