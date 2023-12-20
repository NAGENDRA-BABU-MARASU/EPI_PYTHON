from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    char_freq_for_letter = {}
    for character in letter_text:
        if character in char_freq_for_letter:
            char_freq_for_letter[character] += 1
        else:
            char_freq_for_letter[character] = 1

    for character in magazine_text:
        if character in char_freq_for_letter:
            char_freq_for_letter[character] -= 1
            if char_freq_for_letter[character] == 0:
                del char_freq_for_letter[character]
                if not char_freq_for_letter:
                    return True
    return not char_freq_for_letter


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
