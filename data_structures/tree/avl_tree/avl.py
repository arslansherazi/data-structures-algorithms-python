from typing import Any

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
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert(node.left_child, data)
        else:
            node.right_child = self.insert(node.right_child, data)

        # balance the tree
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balancing_factor = self.get_balancing_factor(node)

        if balancing_factor > 1:
            # CASE-1 Right Rotation
            if data < node.left_child.data:
                return self.right_rotate(node)

            # CASE-2 Left Right Rotation
            else:
                node.left_child = self.left_rotate(node.left_child)
                return self.right_rotate(node)

        if balancing_factor < -1:
            # CASE-3 Left Rotation
            if data > node.right_child.data:
                return self.left_rotate(node)

            # CASE-4 Right Left Rotation
            else:
                node.right_child = self.right_rotate(node.right_child)
                return self.left_rotate(node)

        return node

    def delete(self, node, data):
        if not root:
            return

        # find the node to be deleted
        if data < node.data:
            node.left_child = self.delete(node.left_child, data)
        elif data > node.data:
            node.right_child = self.delete(node.right_child, data)
        else:
            # delete the node has only one child or no child (leaf node)
            if not node.left_child:
                return node.right_child
            if not node.right_child:
                return node.left_child

            # If the node has two children, place the inorder successor in position of the node to be deleted
            temp = self.min_value_node(node.right_child)
            node.data = temp.data
            node.right_child = self.delete(node.right_child, temp.data)

        if not node:
            return node

        # balance the tree
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balancing_factor = self.get_balancing_factor(node)

        if balancing_factor > 1:
            if self.get_balancing_factor(root.left_child) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left_child)
                return self.right_rotate(root)
        if balancing_factor < -1:
            if self.get_balancing_factor(root.right_child) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right_child)
                return self.left_rotate(root)
        return root

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

    root = avl_tree.insert(data=5)
    root = avl_tree.insert(root, 7)
    root = avl_tree.insert(root, 8)

    print("Pre-order traversal::")
    avl_tree.preorder_traversal(root)

    root = avl_tree.insert(root, 4)
    root = avl_tree.delete(root, 8)

    print("\nPre-order traversal after deletion::")
    avl_tree.preorder_traversal(root)


