class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, prev_data, data):
        temp_node = self.head
        new_node = None
        while temp_node:
            if temp_node.data == prev_data:
                new_node = Node(data)
                new_node.next = temp_node.next
                new_node.prev = temp_node
                temp_node.next.prev = new_node
                temp_node.next = new_node
                break
            temp_node = temp_node.next
        if not new_node:
            print('Data not found')

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node

    def delete(self, data):
        temp_node = self.head
        data_found = False
        while temp_node:
            if temp_node.data == data:
                temp_node.prev.next = temp_node.next
                temp_node.next.prev = temp_node.prev
                data_found = True
                break
            temp_node = temp_node.next
        if not data_found:
            print('Data not found')

    def search(self, data):
        index = 0
        temp_node = self.head
        data_found = False
        while temp_node.next:
            if temp_node.data == data:
                data_found = True
                break
            temp_node = temp_node.next
            index += 1
        if data_found:
            print(f'Data is found at index {index}')
        else:
            print('Data is not found')

    def display(self):
        if not self.head:
            print('No data to display')
            return
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='\t')
            temp_node = temp_node.next
        print()

    def display_reverse(self):
        if not self.head:
            print('No data to display')
            return
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        while temp_node:
            print(temp_node.data, end='\t')
            temp_node = temp_node.prev
        print()
