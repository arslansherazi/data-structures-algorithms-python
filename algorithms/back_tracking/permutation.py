def permutation(data, res):
    if data == 1:
        return res
    else:
        return [
            y + x
            for y in permutation(1, res)
            for x in permutation(data - 1, res)
        ]


if __name__ == '__main__':
    print(permutation(1, ["a", "b", "c"]))
    print(permutation(2, ["a", "b", "c"]))
