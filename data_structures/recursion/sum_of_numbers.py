def calculate_sum(_num: int):
    if _num != 0:
        return _num + calculate_sum(_num - 1)
    return _num


if __name__ == '__main__':
    num = int(input('Enter number::'))
    sum_of_numbers = calculate_sum(num)
    print(sum_of_numbers)
