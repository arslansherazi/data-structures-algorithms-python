class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, prev_data, data):
        temp_node = self.head
        prev_node = None
        while temp_node:
            if temp_node.data == prev_data:
                prev_node = temp_node
                break
            temp_node = temp_node.next
        if prev_node:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            print('Data not found')

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        new_node = Node(data)
        temp_node.next = new_node

    def delete(self, data):
        prev_node = next_node = self.head
        temp_node = None
        while next_node:
            if next_node.data == data:
                temp_node = next_node
                break
            prev_node = next_node
            next_node = next_node.next
        if temp_node:
            prev_node.next = temp_node.next
            temp_node.next = None
        else:
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
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='\t')
            temp_node = temp_node.next
        print()
