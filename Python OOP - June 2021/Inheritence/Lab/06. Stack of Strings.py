from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


stack = Stack()
stack.pop("5")
stack.push("100")
stack.pop("-2")

print(stack)
