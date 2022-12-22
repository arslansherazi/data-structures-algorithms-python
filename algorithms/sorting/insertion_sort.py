""" Complexity --> O(n^2)  """

from algorithms.calculate_time import calculate_time


@calculate_time
def insertion_sort(_data):
    data_length = len(_data)
    for i in range(1, data_length):
        value_to_insert = _data[i]
        hole_position = i

        # sorting sub-array and finds the exact hole position where the value should be inserted
        while hole_position > 0 and _data[hole_position - 1] > value_to_insert:
            _data[hole_position] = _data[hole_position - 1]
            hole_position -= 1

        # adds the next element to correct position
        _data[hole_position] = value_to_insert
    return _data


if __name__ == '__main__':
    data = [20, 1, 13, 6, -8, 12, 90, -1, 94, 34, 89, 92, 45, 5, 9, 12, 0, 34]
    sorted_data = insertion_sort(data)
    print(sorted_data)
