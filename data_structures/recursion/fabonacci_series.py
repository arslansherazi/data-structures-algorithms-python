def fabonacci_series(num1, num2, _count):
    # termination condition / base criteria
    if _count == 20:
        return
    next_fabonacci_number = num1 + num2
    print(next_fabonacci_number, end='\t')
    fabonacci_series(num2, next_fabonacci_number, _count + 1)


if __name__ == '__main__':
    count = 1
    f1, f2 = 0, 1
    print(f1, end='\t')
    print(f2, end='\t')
    fabonacci_series(f1, f2, count)

# No of steps = 2 ^ no of disks - 1
