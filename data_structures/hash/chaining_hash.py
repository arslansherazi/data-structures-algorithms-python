from data_structures.linked_list.singly_linked_list import LinkedList


class ChainingHash(object):
    def __init__(self, size: int):
        self.__hash_table = [None for i in range(size)]
        self.hash_value = len(self.__hash_table)

    def __hash_function(self, key):
        if isinstance(key, str):
            key = hash(key)
        hash_table_index = key % self.hash_value
        return hash_table_index

    def insert(self, key, value):
        hash_table_index = self.__hash_function(key)
        hash_table_value = self.__hash_table[hash_table_index]
        if hash_table_value:
            if isinstance(hash_table_value, LinkedList):
                hash_table_value.append(value)
            else:
                linked_list = LinkedList()
                linked_list.append(hash_table_value)
                linked_list.append(value)
                self.__hash_table[hash_table_index] = linked_list
        self.__hash_table[hash_table_index] = value

    def update(self, key, value):
        pass

    def delete(self, key, value):
        pass

    def get_value(self, key):
        pass

    def display(self):
        for hash_table_value in self.__hash_table:
            if isinstance(hash_table_value, LinkedList):
                hash_table_value.display()
                continue
            print(hash_table_value)


if __name__ == '__main__':
    chaining_hash = ChainingHash(size=5)
    chaining_hash.insert('name', 'Arslan Haider Sherazi')
    chaining_hash.insert('roll_no', 'BSEF14A513')

    chaining_hash.display()
