
from list_node import ListNode

def reverse_singly_linked_list(L):
    prev = None
    current = L
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev