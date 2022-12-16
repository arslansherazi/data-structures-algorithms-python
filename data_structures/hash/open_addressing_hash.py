class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class OpenAddressingHash:
    def __init__(self):
        self.__hash_table = []

    def __hash_function(self, key):
        pass

    def __linear_probing(self, key):
        pass

    def __quadratic_probing(self, key):
        pass

    def __rehashing(self, key):
        pass

    def insert(self, key, value):
        pass

    def update(self, key, value):
        pass

    def delete(self, key):
        pass

    def get_value(self, key):
        pass

    @staticmethod
    def search_key(hash_table_value: list, key) -> int:
        pass

    def display(self):
        pass
