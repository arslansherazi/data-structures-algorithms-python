class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class OpenAddressingHash:
    def __init__(self):
        self.__hash_table = []
