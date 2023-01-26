""" Complexity --> O(nlogn)  """
from algorithms.calculate_time import calculate_time
from data_structures.tree.heap.max_heap import MaxHeap


@calculate_time
def heap_sort(_max_heap, _data):
    data_length = len(_data)

    for i in range(data_length - 1, 0, -1):
        _data[i], _data[0] = _data[0], _data[i]
        _max_heap.max_heapify(_data, i, 0)

    return _data


if __name__ == '__main__':
    data = [20, 1, 13, 6, -8, 12, 90, -1, 94, 34, 89, 92, 45, 5, 9, 12, 0, 34]
    heap_array = []
    max_heap = MaxHeap()
    for ele in data:
        max_heap.insert(_heap_array=heap_array, data=ele)
    sorted_data = heap_sort(max_heap, heap_array)
    print(sorted_data)
