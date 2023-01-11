class Item:
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value


def fractional_knapsack(_weight_limit: int, _items: list) -> float:
    # sort the items on basis of density  => density = item.value / item.weight
    _items.sort(key=lambda _item: _item.value / _item.weight, reverse=True)

    _final_value = 0.0

    for item in _items:
        if item.weight <= _weight_limit:
            _weight_limit -= item.weight
            _final_value += item.value
        else:  # add fractional value of the item
            fractional_value = item.value * (_weight_limit / item.weight)
            _final_value += fractional_value
            break

    return round(_final_value, 2)


if __name__ == '__main__':
    weight_limit = 16
    items = [
        Item(6, 6), Item(10, 2), Item(3, 1), Item(5, 8), Item(1, 3), Item(3, 5)
    ]
    final_value = fractional_knapsack(_weight_limit=weight_limit, _items=items)
    print(final_value)
