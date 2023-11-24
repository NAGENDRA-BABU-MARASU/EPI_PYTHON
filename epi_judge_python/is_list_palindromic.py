from list_node import ListNode
from test_framework import generic_test

def reverse_linked_list(L):
    prev = None
    current = L
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fast = L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first_half_iter = L
    second_half_iter = reverse_linked_list(slow)
    while first_half_iter and second_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter = second_half_iter.next
        first_half_iter = first_half_iter.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
