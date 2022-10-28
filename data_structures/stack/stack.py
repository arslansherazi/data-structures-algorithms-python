"""
- LIFO (Last In First Out)
- FILO (First In Last Out)
"""


class Stack:
    def __init__(self):
        self.top = -1
        self.size = 100
        self.data = []

    def push(self, element):
        if self.is_full():
            print('Stack is full')
        else:
            self.top += 1
            self.data.insert(self.top, element)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            element = self.data[self.top]
            self.top -= 1
            return element

    def is_full(self) -> bool:
        return self.top + 1 == self.size

    def is_empty(self) -> bool:
        return self.top < 0

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.data[self.top]


if __name__ == '__main__':
    stack = Stack()
    print(stack.pop())

    stack.push('Arslan')
    stack.push('Haider')
    stack.push('Sherazi')

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print(stack.pop())

