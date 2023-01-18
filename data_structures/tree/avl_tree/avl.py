from data_structures.tree.binary_search_tree.binary_search_tree import BinarySearchTree


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.__root = None

    def insert(self, node=None, data=None):
        # handle root node
        if not self.__root:
            self.__root = Node(data)
            return self.__root

        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert(node.left_child, data)
        else:
            node.right_child = self.insert(node.right_child, data)

        # balance the tree
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balancing_factor = self.get_balancing_factor(node)

        # CASE-1 Left Rotation
        if balancing_factor < -1 and data > node.right_child.data:
            return self.left_rotate(node)

        # CASE-2 Right Rotation
        if balancing_factor > 1 and data < node.left_child.data:
            return self.right_rotate(node)

        # CASE-3 Left Right Rotation
        if balancing_factor > 1 and data > node.left_child.data:
            node.right_child = self.left_rotate(node)
            return self.right_rotate(node)

        # CASE-4 Right Left Rotation
        if balancing_factor < -1 and data < node.right_child.data:
            node.left_child = self.right_rotate(node)
            return self.left_rotate(node)

    def left_rotate(self, z):
        y = z.right_child
        t2 = y.left_child

        # Perform rotation
        y.left_child = z
        z.right_child = t2

        # Update heights
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

        # Return the new root
        return y

    def right_rotate(self, z):
        y = z.left_child
        t3 = y.right_child

        # Perform rotation
        y.right_child = z
        z.left_child = t3

        # Update heights
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

        # Return the new root
        return y

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def get_balancing_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)


if __name__ == '__main__':
    avl_tree = AVLTree()

    # root node
    root = avl_tree.insert(data=5)

    avl_tree.insert(root, 7)
    avl_tree.insert(root, 8)

    print("Pre-order Traversal::")
    avl_tree.preorder_traversal(root)
