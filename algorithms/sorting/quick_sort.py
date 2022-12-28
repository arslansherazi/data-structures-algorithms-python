""" Complexity --> O(n^2)  """

from algorithms.calculate_time import calculate_time


def partition(_data, low, high):
    pivot = _data[high]

    i = low - 1

    # partition the array such that elements at left side of pivot are less than pivot and greater at the right side
    for j in range(low, high):
        if _data[j] <= pivot:
            i = i + 1
            _data[i], _data[j] = _data[j], _data[i]

    # Swap the pivot element with the greater element specified by i
    _data[i + 1], _data[high] = _data[high], _data[i + 1]

    # Return the position from where partition is done
    return i + 1


def quick_sort(_data, low, high):
    if low < high:
        pi = partition(_data, low, high)
        quick_sort(_data, low, pi - 1)
        quick_sort(_data, pi + 1, high)

    return _data


@calculate_time
def _quick_sort(_data, low, high):
    return quick_sort(_data, low, high)


if __name__ == '__main__':
    # data = [12, 34, 54, 2, 3, 9, 8]  # small data set for debugging
    data = [20, 1, 13, 6, -8, 12, 90, -1, 94, 34, 89, 92, 45, 5, 9, 12, 0, 34]
    sorted_data = _quick_sort(data, 0, len(data) - 1)
    print(sorted_data)
