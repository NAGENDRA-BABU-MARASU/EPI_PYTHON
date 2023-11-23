from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        return []

    for i in range(len(perm) -1 , inversion_point, -1):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])

    return perm

print(next_permutation([6,2,1,5,4,3,0]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
