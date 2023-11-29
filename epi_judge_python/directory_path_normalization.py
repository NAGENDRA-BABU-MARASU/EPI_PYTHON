from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    stack = []
    dir = ''
    res = ''
    res += '/'
    path_len = len(path)
    i = 0
    while i < path_len:
        dir_str = ''
        while (i < path_len and path[i] == '/'):
            i += 1

        while ( i < path_len and path[i] != '/'):
            dir_str += path[i]
            i += 1

        if dir_str == '..':
            if len(stack):
                stack.pop()
        elif dir_str == '.':
            continue
        elif len(dir_str) > 0:
            stack.append(dir_str)

        i += 1

    reverse_stack = []
    while len(stack):
        reverse_stack.append(stack.pop())

    while len(reverse_stack):
        temp = reverse_stack[-1]
        if len(reverse_stack != 1):
            res += (temp + "/")
        else:
            res += temp
        stack.pop()

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
