from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    word_to_latest_index = {}
    nearest_repeated_distance = float('inf')
    for index, word in enumerate(paragraph):
        if word in word_to_latest_index:
            current_distance = index - word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance, current_distance)

        word_to_latest_index[word] = index

    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
