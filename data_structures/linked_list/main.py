from data_structures.linked_list.single_linked_list import LinkedList, Node

if __name__ == '__main__':
    # Single Linked List
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