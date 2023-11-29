from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return getTreeInfo(tree).isBalanced


def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and abs(
        leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1

    height = 1 + max(leftSubTreeInfo.height, rightSubTreeInfo.height)
    return TreeInfo(isBalanced, height)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
