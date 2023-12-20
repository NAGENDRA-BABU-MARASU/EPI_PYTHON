from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    count = 0
    for item in d.items():
        if item[1] %2 != 0:
            count += 1
        if count >= 2:
            return False

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
