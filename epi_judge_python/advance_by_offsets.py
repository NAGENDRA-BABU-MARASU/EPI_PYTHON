from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    print("A : ", A)
    furthest_reach_so_far , last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, i + A[i])
        print("furthest_so_far: ", furthest_reach_so_far)
        print("index: ", i)
        print()
        i += 1

    return furthest_reach_so_far >= last_index

print(can_reach_end([3,3,1,0,2,0,1]))

#
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('advance_by_offsets.py',
#                                        'advance_by_offsets.tsv',
#                                        can_reach_end))
