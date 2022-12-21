from algorithms.calculate_time import calculate_time


@calculate_time
def selection_sort(_data):
    data_length = len(_data)
    for i in range(data_length):
        # find minimum value
        min_value_index = i
        for j in range(i + 1, data_length):
            if _data[j] < _data[min_value_index]:
                min_value_index = j

        # replace min value with sorted array
        if _data[min_value_index] < _data[i]:
            temp = _data[i]
            _data[i] = _data[min_value_index]
            _data[min_value_index] = temp

    return _data


if __name__ == '__main__':
    data = [20, 1, 13, 6, -8, 12, 90, -1, 94, 34, 89, 92, 45, 5, 9, 12, 0, 34]
    sorted_data = selection_sort(data)
    print(sorted_data)
