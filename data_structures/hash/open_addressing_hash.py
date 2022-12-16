class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class OpenAddressingHash:
    def __init__(self, size):
        self.__hash_table = [None for _ in range(size)]
        self.__hash_value = len(self.__hash_table)

    def __hash_function(self, key):
        if isinstance(key, str):
            key = hash(key)
        hash_table_index = key % self.__hash_value
        if self.__hash_table[hash_table_index]:
            hash_table_index = self.__linear_probing(current_index=hash_table_index)
        return hash_table_index

    def __linear_probing(self, current_index):
        counter = 1
        while True:
            hash_table_index = (current_index + counter) % self.__hash_value
            if not self.__hash_table[hash_table_index]:
                return hash_table_index
            # if no index is free then increase array size
            if counter == len(self.__hash_table):
                self.__hash_table.extend([None for i in range(self.__hash_value)])
                self.__hash_value = len(self.__hash_table)
            counter += 1

    def __quadratic_probing(self, key):
        pass

    def __double_hashing(self, key):
        pass

    def insert(self, key, value):
        hash_table_index = self.__hash_function(key)
        node = Node(key, value)
        self.__hash_table[hash_table_index] = node

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
        for node in self.__hash_table:
            if not node:
                print(None)
                continue
            print(node.key, "  -->  ", node.value)


if __name__ == '__main__':
    open_addressing_hash = OpenAddressingHash(size=5)
    open_addressing_hash.insert('name', 'Arslan Haider Sherazi')
    open_addressing_hash.insert('designation', 'Software Engineer')
    open_addressing_hash.insert('tech', 'python')
    open_addressing_hash.insert('age', 27)
    open_addressing_hash.insert('address', 'Lahore')
    open_addressing_hash.insert('email', 'arslanhaider.dev@hotmail.com')
    open_addressing_hash.insert('company', 'Folio3')

    open_addressing_hash.display()

    # print()
    # print(open_addressing_hash.get_value('name'))
    # # print(chaining_hash.get_value('address2'))
    #
    # print()
    # open_addressing_hash.update('name', 'Syed Arslan Haider')
    #
    # print()
    # open_addressing_hash.display()
    #
    # print()
    # print(open_addressing_hash.get_value('name'))
    #
    # open_addressing_hash.delete('company')
    # print()
    # open_addressing_hash.display()
