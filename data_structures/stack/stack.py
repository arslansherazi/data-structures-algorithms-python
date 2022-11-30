"""
- LIFO (Last In First Out)
- FILO (First In Last Out)
"""


class Queue:
    def __init__(self):
        self.__top = -1
        self.size = 10
        self.__data = []

    def push(self, element):
        if self.is_full():
            print('Stack is full')
        else:
            self.__top += 1
            self.__data.insert(self.__top, element)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            element = self.__data[self.__top]
            self.__top -= 1
            return element

    def is_full(self) -> bool:
        return self.__top + 1 == self.size

    def is_empty(self) -> bool:
        return self.__top < 0

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.__data[self.__top]

    def get_stack_size(self) -> int:
        return len(self.__data)


if __name__ == '__main__':
    stack = Queue()
    print(stack.pop())

    stack.push('Arslan')
    stack.push('Haider')
    stack.push('Sherazi')
    stack.push('1')
    stack.push('2')

    for i in range(stack.get_stack_size()):
        print(stack.pop())
