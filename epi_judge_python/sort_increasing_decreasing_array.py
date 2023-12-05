from typing import List
import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    for i, it in enumerate(sorted_arrays_iters):
        next_element = next(it, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_entry_i = heapq.heappop(min_heap)
        result.append(smallest_entry)
        smallest_entry_iter = sorted_arrays_iters[smallest_entry_i]
        next_element = next(smallest_entry_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_entry_i))

    return result


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_sub_arrays = []
    INCREASING, DECREASING = (0, 1)
    subarray_type = INCREASING
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or
                (A[i - 1] < A[i] and subarray_type == DECREASING) or
                (A[i - 1] >= A[i] and subarray_type == INCREASING)):
            sorted_sub_arrays.append(A[start_idx:i] if subarray_type == INCREASING else
                                     A[i - 1: start_idx - 1: -1])
            start_idx = i 
            subarray_type = (DECREASING if subarray_type == INCREASING else INCREASING)

    return merge_sorted_arrays(sorted_sub_arrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
