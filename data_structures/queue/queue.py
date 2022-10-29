import random


class Queue:
    def __init__(self, size):
        self.size = size
        self.__data = []
        self.__front = 0
        self.__rear = 0

    def enqueue(self, ele):
        if self.is_full():
            print('Queue is full')
            return
        else:
            self.__data.insert(self.__rear, ele)
            ele = self.__data[self.__rear]
            self.__rear += 1
            return ele

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return
        else:
            ele = self.__data[self.__front]
            self.__front += 1
            if self.__front >= self.__rear:
                self.__front = self.__rear = 0
            return ele

    def is_full(self) -> bool:
        return self.__rear == self.size

    def is_empty(self) -> bool:
        return self.__rear == 0

    def front(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            return self.__data[self.__front]

    def rear(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            return self.__data[self.__rear]

    def get_queue_data(self) -> list:
        return self.__data[self.__front:self.__rear]


if __name__ == '__main__':
    queue_size = 10
    queue = Queue(size=queue_size)

    print('################# ENQUEUE #################')
    for i in range(queue_size):
        random_number = random.randint(1, 1000)
        print(f'{queue.enqueue(random_number)} is Enqueued --> {queue.get_queue_data()}')

    print('################# DEQUEUE #################')
    for i in range(queue_size):
        print(f'{queue.dequeue()} is Dequeued --> {queue.get_queue_data()}')

    print()
    print(f'{queue.enqueue(100)} is Enqueued --> {queue.get_queue_data()}')
