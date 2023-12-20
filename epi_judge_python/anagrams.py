from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagrams = {}
    for string in dictionary:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    result = []
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            result.append(anagrams[key])

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
