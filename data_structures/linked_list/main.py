from data_structures.linked_list.double_linked_list import DoubleLinkedList
from data_structures.linked_list.single_linked_list import LinkedList, Node

if __name__ == '__main__':
    # Single Linked List
    print('#################### SINGLE LINKED LIST ####################')


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
