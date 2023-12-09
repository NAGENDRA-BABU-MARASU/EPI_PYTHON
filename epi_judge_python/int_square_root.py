from test_framework import generic_test


def square_root(k: int) -> int:
    left = 0
    right = k

    while left <= right:
        middle = (left + right) // 2
        if middle**2 > k:
            right = middle - 1
        else:
            left = middle + 1
    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
