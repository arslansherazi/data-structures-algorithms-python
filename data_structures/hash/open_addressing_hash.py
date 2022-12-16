class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class OpenAddressingHash:
    def __init__(
            self, size: int, is_linear_probing: bool = False, is_quadratic_probing: bool = False,
            is_rehashing: bool = bool
    ):
        self.__hash_table = [None for _ in range(size)]
        self.__hash_value = len(self.__hash_table)
        self.__second_hash_value = 1 + self.__hash_value * 2
        self.is_linear_probing = is_linear_probing
        self.is_quadratic_probing = is_quadratic_probing

    def __hash_function(self, key):
        if isinstance(key, str):
            key = hash(key)
        hash_table_index = key % self.__hash_value
        if self.__hash_table[hash_table_index]:
            hash_table_index = self.__probing(key, current_index=hash_table_index)
        return hash_table_index

    def __second_hash_function(self, key):
        if isinstance(key, str):
            key = hash(key)
        hash_table_index = key % self.__second_hash_value
        return hash_table_index

    def __probing(self, key, current_index, is_insert=True):
        counter = 1
        hash_table_indices = set()
        while True:
            if self.is_linear_probing:
                probe_value = counter
            elif self.is_quadratic_probing:
                probe_value = counter * counter
            else:  # Double Hashing
                probe_value = counter * self.__second_hash_function(key)

            hash_table_index = (current_index + probe_value) % self.__hash_value
            node = self.__hash_table[hash_table_index]

            if not node:
                if is_insert:
                    return hash_table_index
            else: # check key in case of not insertion
                if node.key == key:
                    return hash_table_index

            # in case of get, update, delete check if all indexes of array are explored then key is not present
            if not is_insert:
                hash_table_indices.add(hash_table_index)
                if len(hash_table_indices) == len(self.__hash_table):
                    return

            # if no index is free then increase array size in case of insert only
            if counter == len(self.__hash_table) and is_insert:
                self.__hash_table.extend([None for i in range(self.__hash_value)])
                self.__hash_value = len(self.__hash_table)
                self.__second_hash_value = 1 + self.__hash_value * 2
            counter += 1

    def insert(self, key, value):
        hash_table_index = self.__hash_function(key)
        node = Node(key, value)
        self.__hash_table[hash_table_index] = node

    def update(self, key, value):
        node, hash_table_index = self.__get_node_data(key)
        if node:
            node.value = value
            self.__hash_table[hash_table_index] = node
            return
        print('Key not found')

    def delete(self, key):
        pass

    def get_value(self, key):
        node, _ = self.__get_node_data(key)
        if node:
            return node.value
        return 'Key not found'

    def __get_node_data(self, key):
        hash_table_index = self.__hash_function(key)
        node = self.__hash_table[hash_table_index]
        if not node or node.key != key:
            hash_table_index = self.__probing(key, current_index=hash_table_index, is_insert=False)
            if hash_table_index is None:
                return
            else:
                node = self.__hash_table[hash_table_index]
        return node, hash_table_index

    @staticmethod
    def search_key(hash_table_value: list, key) -> int:
        pass

    def display(self):
        for node in self.__hash_table:
            if not node:
                print(None)
                continue
            print(node.key, "  -->  ", node.value)


if __name__ == '__main__':
    open_addressing_hash = OpenAddressingHash(size=5, is_quadratic_probing=True)

    open_addressing_hash.insert('name', 'Arslan Haider Sherazi')
    open_addressing_hash.insert('designation', 'Software Engineer')
    open_addressing_hash.insert('tech', 'python')
    open_addressing_hash.insert('age', 27)
    open_addressing_hash.insert('address', 'Lahore')
    open_addressing_hash.insert('email', 'arslanhaider.dev@hotmail.com')
    open_addressing_hash.insert('company', 'Folio3')

    open_addressing_hash.display()

    print()
    print(open_addressing_hash.get_value('name'))
    print(open_addressing_hash.get_value('address2'))


    print()
    open_addressing_hash.update('name', 'Syed Arslan Haider')

    print()
    open_addressing_hash.display()

    # print()
    # print(open_addressing_hash.get_value('name'))
    #
    # open_addressing_hash.delete('company')
    # print()
    # open_addressing_hash.display()
