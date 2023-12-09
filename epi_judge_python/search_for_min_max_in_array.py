import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

# MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]):
    # TODO - you fill in here.
    def min_max(a,b):
        return (a,b) if a < b else (b,a)
    if len(A) <= 1:
        return (A[0], A[0])

    global_min_max = min_max(A[0], A[1])
    for i in range(2, len(A) - 1, 2):
        local_min_max = min_max(A[i], A[i+1])
        global_min_max = (
            min(global_min_max[0], local_min_max[0]),
            max(global_min_max[1], local_min_max[1])
        )


    if len(A) % 2 != 0:
        global_min_max = (
            min(global_min_max[0], A[-1]),
            max(global_min_max[1], A[-1])
        )

    return global_min_max




def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
