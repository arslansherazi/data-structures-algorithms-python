class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ChainingHash:
    def __init__(self, size: int):
        self.__hash_table = [[] for _ in range(size)]
        self.__hash_value = len(self.__hash_table)

    def __hash_function(self, key):
        if isinstance(key, str):
            key = hash(key)
        hash_table_index = key % self.__hash_value
        return hash_table_index

    def insert(self, key, value):
        node = Node(key, value)
        hash_table_index = self.__hash_function(key)
        hash_table_value = self.__hash_table[hash_table_index]
        if hash_table_value:
            hash_table_value.append(node)
            self.__hash_table[hash_table_index] = hash_table_value
        else:
            self.__hash_table[hash_table_index] = [node]

    def update(self, key, value):
        pass

    def delete(self, key, value):
        pass

    def get_value(self, key):
        hash_table_index = self.__hash_function(key)
        hash_table_value = self.__hash_table[hash_table_index]
        if hash_table_value:
            node_index = self.search_key(hash_table_value, key)
            if node_index or node_index == 0:
                return hash_table_value[node_index].value
        raise Exception(f'Key Error. {key} not found in hash')

    @staticmethod
    def search_key(hash_table_value: list, key) -> int:
        for node_index, node in enumerate(hash_table_value):
            if node.key == key:
                return node_index

    def display(self):
        for hash_table_value in self.__hash_table:
            if not hash_table_value:
                print([])
                continue
            for _index, node in enumerate(hash_table_value):
                if _index == len(hash_table_value) - 1:
                    print(node.value, end='')
                    break
                print(node.value, end='  -->  ')
            print()


if __name__ == '__main__':
    chaining_hash = ChainingHash(size=5)
    chaining_hash.insert('name', 'Arslan Haider Sherazi')
    chaining_hash.insert('designation', 'Software Engineer')
    chaining_hash.insert('tech', 'python')
    chaining_hash.insert('age', 27)
    chaining_hash.insert('address', 'Lahore')
    chaining_hash.insert('email', 'arslanhaider.dev@hotmail.com')
    chaining_hash.insert('company', 'Folio3')

    chaining_hash.display()

    print()
    print(chaining_hash.get_value('name'))
    print(chaining_hash.get_value('address2'))
