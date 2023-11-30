class BinaryTreeNode:
    def __init__(self, data=None, name=None, left=None, right=None):
        self.data = data
        self.name = name
        self.left = left
        self.right = right


def root_to_leaf_sum_return_paths(tree, remaining_weight, all_paths=[], current_path=[]):
    if not tree:
        return False


    if not tree.left and not tree.right:
        if remaining_weight == tree.data:
            current_path.append(tree.name)
            all_paths.append(current_path)


    root_to_leaf_sum_return_paths(tree.left, remaining_weight - tree.data, all_paths, current_path + [tree.name])
    root_to_leaf_sum_return_paths(tree.right, remaining_weight - tree.data, all_paths, current_path + [tree.name])
    return all_paths


D = BinaryTreeNode(28, 'D')
E = BinaryTreeNode(0, 'E')
C = BinaryTreeNode(271, 'C', D, E)
H = BinaryTreeNode(17, 'H')
G = BinaryTreeNode(3, 'G', H)
F = BinaryTreeNode(561, 'F', None, G)
M = BinaryTreeNode(641, 'M')
L = BinaryTreeNode(401, 'L', None, M)
N = BinaryTreeNode(257, 'N')
K = BinaryTreeNode(1, 'K', L, N)
J = BinaryTreeNode(2, 'J', None, K)
P = BinaryTreeNode(28, 'P')
O = BinaryTreeNode(271, 'O', None, P)
I = BinaryTreeNode(6, 'I', J, O)
B = BinaryTreeNode(6, 'B', C, F)
A = BinaryTreeNode(314, 'A', B, I)

print(root_to_leaf_sum_return_paths(A, 619))
