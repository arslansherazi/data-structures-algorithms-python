from data_structures.linked_list.double_linked_list import DoubleLinkedList
from data_structures.linked_list.single_linked_list import LinkedList, Node

if __name__ == '__main__':
    # Single Linked List
    print('#################### SINGLE LINKED LIST ####################')
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

    # Double Linked List
    print('#################### DOUBLE LINKED LIST ####################')
    double_linked_list = DoubleLinkedList()

    double_linked_list.push(1)
    double_linked_list.push(2)
    double_linked_list.push(3)
    double_linked_list.display()
    double_linked_list.display_reverse()

    double_linked_list.append(10)
    double_linked_list.append(20)
    double_linked_list.append(30)
    double_linked_list.display()
    double_linked_list.display_reverse()

    double_linked_list.insert(10, 101)
    double_linked_list.display()
    double_linked_list.display_reverse()

    double_linked_list.search(1000)
    double_linked_list.search(101)

    double_linked_list.delete(20)
    double_linked_list.display()
    double_linked_list.display_reverse()
