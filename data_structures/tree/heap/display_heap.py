import math
from io import StringIO


def show_heap(heap_array, total_width=50, fill=' '):
    """
    Show Heap
    """
    output = StringIO()
    last_row = -1
    print('-' * total_width)
    for i, n in enumerate(heap_array):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print()
    print('-' * total_width)
