""" Complexity --> O(nlogn)  """

from algorithms.calculate_time import calculate_time


def merge_sort(_data):
    if len(_data) > 1:
        mid = len(_data) // 2

        # dividing the data array into 2 halves
        left_side = _data[:mid]
        right_side = _data[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        merge(_data, left_side, right_side)


def merge(_data, left_side, right_side):
        i = j = k = 0

        # sorting the sub array and merge
        while i < len(left_side) and j < len(right_side):
            if left_side[i] <= right_side[j]:
                _data[k] = left_side[i]
                i += 1
            else:
                _data[k] = right_side[j]
                j += 1
            k += 1

        # check if any element is left
        while i < len(left_side):
            _data[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            _data[k] = right_side[j]
            j += 1
            k += 1


@calculate_time
def _merge_sort():
    data = [20, 1, 13, 6, -8, 12, 90, -1, 94, 34, 89, 92, 45, 5, 9, 12, 0, 34]
    merge_sort(data)
    print(data)


if __name__ == '__main__':
    _merge_sort()
