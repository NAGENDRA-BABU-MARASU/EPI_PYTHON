from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    if not tree:
        return result

    queue = []
    queue.append(tree)
    while queue:
        level = []
        for i in range(len(queue)):
            current = queue.pop(0)
            level.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result.append(level)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
