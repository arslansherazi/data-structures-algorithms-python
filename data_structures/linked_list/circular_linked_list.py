class Node:
    def __init__(self, data):
        self.next = self
        self.prev = self
        self.data = data


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, prev_data, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next != self.head:
                if temp_node.data == prev_data:
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
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node

    def delete(self, data):
        temp_node = self.head
        data_found = False
        # handle head node
        if temp_node.data == data:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next
            temp_node.next = None
            temp_node.prev = None
        # handle last node
        elif temp_node.prev.data == data:
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
            self.head.prev.next = None
            self.head.prev.prev = None
        else:
            while temp_node.next != self.head:
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
        while temp_node.next != self.head:
            if temp_node.data == data:
                data_found = True
                break
            temp_node = temp_node.next
            index += 1
        if temp_node.data == data:
            data_found = True
        if data_found:
            print(f'Data is found at index {index}')
        else:
            print('Data is not found')

    def display(self):
        if not self.head:
            print('No data to display')
            return
        temp_node = self.head
        while temp_node.next != self.head:
            print(temp_node.data, end='\t')
            temp_node = temp_node.next
        print(temp_node.data, end='\t')
        print()

    def display_reverse(self):
        if not self.head:
            print('No data to display')
            return
        temp_node = self.head.prev
        print('Reverse:', end='\t')
        while temp_node != self.head:
            print(temp_node.data, end='\t')
            temp_node = temp_node.prev
        print(temp_node.data, end='\t')
        print()


if __name__ == '__main__':
    circular_linked_list = CircularLinkedList()

    circular_linked_list.push(1)
    circular_linked_list.push(2)
    circular_linked_list.push(3)
    circular_linked_list.display()
    circular_linked_list.display_reverse()

    circular_linked_list.append(10)
    circular_linked_list.append(20)
    circular_linked_list.append(30)
    circular_linked_list.display()
    circular_linked_list.display_reverse()

    circular_linked_list.insert(10, 101)
    circular_linked_list.display()
    circular_linked_list.display_reverse()

    circular_linked_list.search(1000)
    circular_linked_list.search(30)

    circular_linked_list.delete(3)
    circular_linked_list.display()
    circular_linked_list.display_reverse()
