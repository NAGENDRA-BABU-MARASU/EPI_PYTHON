import string

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x = x // 10
        if x <= 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    running_sum = 0
    is_negative = False
    if s[0] == '-':
        is_negative = True

    is_positive = s[0] == '+'

    if is_negative or is_positive:
        for i in range(1, len(s)):
            running_sum = running_sum * 10 + ord(s[i]) - ord('0')
    elif not is_negative:
        for i in range(len(s)):
            running_sum = running_sum * 10 + ord(s[i]) - ord('0')

    return -1 * running_sum if is_negative else running_sum




def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
