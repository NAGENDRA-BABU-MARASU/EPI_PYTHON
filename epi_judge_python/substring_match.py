from test_framework import generic_test
import functools


def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1
    BASE = 26

    def compute_hash(s):
        string_hash = 0
        for c in s:
            string_hash = (string_hash * BASE) + ord(c)
        return string_hash

    t_hash = compute_hash(t[:len(s)])
    s_hash = compute_hash(s)
    power_s = BASE ** max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i-len(s): i] == s:
            return i - len(s)

        t_hash = t_hash - ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

    if t_hash == s_hash and t[-len(s) : ] == s:
        return len(t) - len(s)

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
