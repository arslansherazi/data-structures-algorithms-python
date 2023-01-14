class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class BinarySearchTree:
    def __init__(self):
        self.__root = None
        
    def insert(self, node=None, data=None):
        if not self.__root:
            self.__root = Node(data)
            return self.__root
            
        # handle root node
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert(node.left_child, data)
        else:
            node.right_child = self.insert(node.right_child, data)

        return node

    def update(self, data):
        pass

    def delete(self, data):
        pass

    def search(self, node, data):
        # handle empty tree
        if not self.__root:
            print('Tree is empty')
            return
        if not node:
            return
        if node.data == data:
            return self.__root.data
        if data < node.data:
            return self.search(node.left_child, data)
        else:
            return self.search(node.right_child, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left_child)
            print(str(node.data) + ' -> ', end='')
            self.inorder_traversal(node.right_child)

    def preorder_traversal(self, node):
        if node:
            print(str(node.data) + ' -> ', end='')
            self.inorder_traversal(node.left_child)
            self.inorder_traversal(node.right_child)

    def postorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left_child)
            self.inorder_traversal(node.right_child)
            print(str(node.data) + ' -> ', end='')


if __name__ == '__main__':
    bst = BinarySearchTree()

    # root node
    root = bst.insert(data=12)

    bst.insert(root, 9)
    bst.insert(root, 8)
    bst.insert(root, 2)
    bst.insert(root, 6)
    bst.insert(root, 10)
    bst.insert(root, 13)
    bst.insert(root, 4)
    bst.insert(root, 16)
    bst.insert(root, 17)

    # tree traversal
    print('Inorder Traversal:')
    bst.inorder_traversal(root)

    print('\nPreorder Traversal:')
    bst.preorder_traversal(root)

    print('\nPostorder Traversal:')
    bst.postorder_traversal(root)

    # search data in tree
    if not bst.search(root, data=15):
        print('\nData not exist in the tree')
    else:
        print('\nData is present in the tree')
