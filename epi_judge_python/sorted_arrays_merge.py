import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        next_element = next(it, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_entry_i = heapq.heappop(min_heap)
        smallest_entry_iter = sorted_arrays_iters[smallest_entry_i]
        result.append(smallest_entry)
        next_element = next(smallest_entry_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element , smallest_entry_i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
