from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # result = []
    # if not tree:
    #     return result
    #
    # def preorder_traversal_helper(tree, result):
    #     if tree:
    #         result.append(tree.data)
    #     if tree.left:
    #         preorder_traversal_helper(tree.left, result)
    #     if tree.right:
    #         preorder_traversal_helper(tree.right, result)
    #
    #     return result
    #
    # return preorder_traversal_helper(tree, result)
    stack = [tree]
    result = []
    while stack:
        curr = stack.pop()
        if curr:
            result.append(curr.data)
            stack.append(curr.right)
            stack.append(curr.left)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
