""" Complexity --> O(n)  """

from algorithms.calculate_time import calculate_time


@calculate_time
def shell_sort(_data):
    data_length = len(_data)
    interval = data_length // 2

    while interval > 0:
        for i in range(interval, data_length):
            temp = _data[i]
            j = i

            # comparing the values with intervals (gaps) and sort
            while j >= interval and _data[j - interval] > temp:
                _data[j] = _data[j - interval]  # _data[j] = right side, _data[j - interval] = left side
                j -= interval
            _data[j] = temp
        interval //= 2

    return _data


if __name__ == '__main__':
    data = [12, 34, 54, 2, 3, 9, 8]
    sorted_data = shell_sort(data)
    print(sorted_data)
