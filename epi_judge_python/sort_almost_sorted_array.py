import itertools
from typing import Iterator, List

from test_framework import generic_test
import heapq

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    result = []
    min_heap = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
