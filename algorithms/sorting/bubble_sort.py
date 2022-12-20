from algorithms.calculate_time import calculate_time


@calculate_time
def bubble_sort(_data):
    data_length = len(_data)
    for i in range(data_length):
        swapped = False
        for j in range(data_length - i - 1) :
            if _data[j] > _data[j+1]:
                temp = _data[j]
                _data[j] = _data[j+1]
                _data[j+1] = temp
                swapped = True
        if not swapped:
            break
    return _data


if __name__ == '__main__':
    data = [20, 1, 13, 6, -8, 12, 90, -1, 94, 34, 89, 92, 45, 5, 9, 12, 0, 34]
    sorted_data = bubble_sort(data)
    print(sorted_data)
