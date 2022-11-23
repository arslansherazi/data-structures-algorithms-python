class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, prev_data, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp_node = self.head
            prev_node = None
            while temp_node:
                if temp_node.data == prev_data:
                    prev_node = temp_node
                    break
                temp_node = temp_node.next
            if prev_node:
                new_node.next = prev_node.next
                prev_node.next = new_node
            else:
                print('\nData not found')

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
            print('\nData not found')

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
            print(f'\nData is found at index {index}')
        else:
            print('\nData is not found')

    def display(self):
        if not self.head:
            print('\nNo data to display')
            return
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='\t')
            temp_node = temp_node.next
        print()

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == '__main__':
    linked_list = LinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linked_list.head = node1
    node1.next = node2
    node2.next = node3

    linked_list.display()

    linked_list.push(10)
    linked_list.push(20)

    linked_list.display()

    linked_list.insert(100, 200)
    linked_list.insert(2, 21)
    linked_list.display()

    linked_list.delete(200)
    linked_list.delete(21)
    linked_list.display()

    linked_list.append(89)
    linked_list.append(91)
    linked_list.display()

    linked_list.search(89)

    linked_list.reverse()
    linked_list.display()
