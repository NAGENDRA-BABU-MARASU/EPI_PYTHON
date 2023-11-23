from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    answer = 0
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in range(len(s)):
        if i < len(s) -1 and values[s[i]] < values[s[i+1]]:
            answer -= values[s[i]]
        else:
            answer += values[s[i]]

    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
