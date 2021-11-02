class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            return
        self.data.append(element)

    def pop(self):
        if not self.data:
            return
        return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        return not len(self.data) > 0

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"


my_stack = Stack()

my_stack.push("some value")
print(my_stack)
print(my_stack.data)
print(my_stack.pop())
print(my_stack.is_empty())