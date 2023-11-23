from test_framework import generic_test


def snake_string(s: str) -> str:
    rows = [[] for i in range(3)]
    index = 1
    step = -1
    for char in s:
        rows[index].append(char)
        if index == 0:
            step = 1
        elif index == 3-1:
            step = -1
        index += step
    for i in range(len(rows)):
        rows[i] = ''.join(rows[i])

    result_string = ''
    for row in rows:
        result_string += row

    return result_string


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
