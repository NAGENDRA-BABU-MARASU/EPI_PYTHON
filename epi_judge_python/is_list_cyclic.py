import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:

    def get_starting_node(slow_ptr, fast_ptr):
        while slow_ptr is not fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return slow_ptr


    def cycle_len(end):
        start = end
        length = 0
        while True:
            length += 1
            start = start.next
            if start is end:
                return length

    slow = head
    fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        # if slow is fast:
        #     cycle_len_advanced_iterator = head
        #     cycle_length = cycle_len(slow)
        #     for _ in range(cycle_length):
        #         cycle_len_advanced_iterator = cycle_len_advanced_iterator.next
        #
        #     it = head
        #     while it is not cycle_len_advanced_iterator:
        #         it = it.next
        #         cycle_len_advanced_iterator = cycle_len_advanced_iterator.next
        #     return it

        if slow is fast:
            return get_starting_node(slow, fast)

    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
