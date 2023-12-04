def invert_binary_tree(tree):
    if not tree:
        return None

    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    tree.left, tree.right = tree.right, tree.left
    return tree