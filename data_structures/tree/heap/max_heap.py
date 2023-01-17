class MaxHeap:
    def heapify(self, _heap_array, _heap_array_size, _root_node_index):
        largest_node_index = _root_node_index
        left_child_index = 2 * _root_node_index + 1
        right_child_index = 2 * _root_node_index + 2

        if left_child_index < _heap_array_size and _heap_array[_root_node_index] < _heap_array[left_child_index]:
            largest_node_index = left_child_index

        if right_child_index < _heap_array_size and _heap_array[largest_node_index] < _heap_array[right_child_index]:
            largest_node_index = right_child_index

        if largest_node_index != _root_node_index:
            _heap_array[_root_node_index], _heap_array[largest_node_index] = _heap_array[largest_node_index], _heap_array[_root_node_index]
            self.heapify(_heap_array, _heap_array_size, largest_node_index)

    def insert(self, _heap_array, data):
        size = len(_heap_array)
        if size == 0:
            _heap_array.append(data)
        else:
            _heap_array.append(data)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(_heap_array, size, i)

    def delete(self, _heap_array, data):
        size = len(_heap_array)
        i = 0
        for i in range(0, size):
            if data == _heap_array[i]:
                break

        _heap_array[i], _heap_array[size - 1] = _heap_array[size - 1], _heap_array[i]

        _heap_array.remove(data)

        for i in range((len(_heap_array) // 2) - 1, -1, -1):
            self.heapify(_heap_array, len(_heap_array), i)


if __name__ == '__main__':
    heap_array = []

    max_heap = MaxHeap()

    max_heap.insert(heap_array, 4)
    max_heap.insert(heap_array, 5)
    max_heap.insert(heap_array, 7)
    max_heap.insert(heap_array, 9)
    max_heap.insert(heap_array, 10)
    max_heap.insert(heap_array, 8)
    max_heap.insert(heap_array, 6)

    print(f'Heap Array before deletion: {heap_array}')

    max_heap.delete(heap_array, 5)

    print(f'Heap Array after deletion: {heap_array}')
