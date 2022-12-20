""" Complexity --> O(log(logn))  """
from algorithms.calculate_time import calculate_time


@calculate_time
def interpolation_search(_data, _element):
    lower_bound = 0
    upper_bound = len(_data) - 1

    while True:
        if upper_bound < lower_bound:
            return  # element not found

        mid_point = lower_bound + (
                (upper_bound - lower_bound) / (data[upper_bound] - data[lower_bound])
        ) * (_element - data[lower_bound])

        if not isinstance(mid_point, int):
            mid_point = int(mid_point)

        if _data[mid_point] == _element:
            return mid_point

        if _element > _data[mid_point]:
            lower_bound = mid_point - 1
        else:
            upper_bound = mid_point - 1


if __name__ == '__main__':
    data = [1, 3, 6, 8, 12, 90, -1, 94, 34, 89, 92, 45, 5, 9, 12]
    data.sort()  # data array should be sorted for binary search
    element = 45
    index = interpolation_search(_data=data, _element=element)
    if index > -1:
        print(f'{element} is present at index {index}')
    else:
        print(f'{element} does not exist in the data')
