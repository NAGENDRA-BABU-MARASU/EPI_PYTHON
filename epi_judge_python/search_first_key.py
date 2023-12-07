from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    left = 0
    right = len(A) -1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == k:
            result = mid
            right = mid - 1
        elif k > A[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
