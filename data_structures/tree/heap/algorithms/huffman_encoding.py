import base64

from bitarray import bitarray


class NodeTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return f'{self.left}_{self.right}'


class HuffmanEncoding:
    def huffman_code_tree(self, _node, binary_data=''):
        if isinstance(_node, str):
            return {_node: bitarray(binary_data)}
        left_child, right_child = _node.children()
        encoded_data = dict()
        encoded_data.update(self.huffman_code_tree(left_child, binary_data=binary_data + '0'))
        encoded_data.update(self.huffman_code_tree(right_child, binary_data=binary_data + '1'))
        return encoded_data

    @staticmethod
    def calculate_frequency(data: str) -> list:
        """
        Calculates frequencies

        :param data: string data

        :return: frequencies map
        """
        _frequencies = {}
        for _char in data:
            if _char in _frequencies:
                _frequencies[_char] += 1
            else:
                _frequencies[_char] = 1

        _frequencies = sorted(_frequencies.items(), key=lambda x: x[1], reverse=True)

        return _frequencies

    def get_huffman_tree(self, data: str):
        """
        Gets huffman encoded data tree

        :param data: encoded data
        :return: huffman codes tree
        """
        frequencies = self.calculate_frequency(data=data)

        nodes = frequencies

        while len(nodes) > 1:
            key1, c1 = nodes[-1]
            key2, c2 = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

        huffman_tree = huffman_encoding.huffman_code_tree(nodes[0][0])

        return huffman_tree

    @staticmethod
    def encode_data(huffman_tree: dict, data: str) -> bitarray:
        """
        Encode the data using huffman encoding

        :param data: data to be encoded
        :param huffman_tree: huffman tree

        :return: huffman encoded data
        """
        encoded_data = bitarray()
        encoded_data.encode(huffman_tree, data)
        return encoded_data

    @staticmethod
    def decode_data(huffman_tree: dict, encoded_data: bitarray) -> str:
        """
        Decode data

        :param encoded_data: huffman encoded data
        :param huffman_tree: huffman tree

        :return: decoded data
        """
        decoded_data = bitarray(encoded_data).decode(huffman_tree)
        return ''.join(decoded_data)


if __name__ == '__main__':
    huffman_encoding = HuffmanEncoding()

    # compress image
    with open("test_image.png", "rb") as image_file:
        image_data = base64.b64encode(image_file.read())

    print(f'Size of data before encoding: {round(len(image_data) / 1024)} KB')

    _huffman_tree = huffman_encoding.get_huffman_tree(data=image_data.decode())

    encoded_image_data = huffman_encoding.encode_data(huffman_tree=_huffman_tree, data=image_data.decode())

    print(f'Size of data after encoding: {encoded_image_data.nbytes / 1024} KB')

    decoded_image_data = huffman_encoding.decode_data(huffman_tree=_huffman_tree, encoded_data=encoded_image_data)


