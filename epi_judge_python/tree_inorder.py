from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    if not tree:
        return result

    def inorder_traversal_helper(tree, result):
        if tree.left:
            inorder_traversal_helper(tree.left, result)
        if tree:
            result.append(tree.data)
        if tree.right:
            inorder_traversal_helper(tree.right, result)

        return result

    return inorder_traversal_helper(tree, result)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
