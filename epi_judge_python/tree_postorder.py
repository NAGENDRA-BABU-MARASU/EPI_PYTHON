from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # result = []
    # if not tree:
    #     return result
    #
    # def postorder_traversal_helper(tree, result):
    #     if tree.left:
    #         postorder_traversal_helper(tree.left, result)
    #     if tree.right:
    #         postorder_traversal_helper(tree.right, result)
    #     if tree:
    #         result.append(tree.data)
    #
    #     return result
    #
    # return postorder_traversal_helper(tree, result)
    result = []
    stack = []
    while stack or tree:
        if tree:



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
