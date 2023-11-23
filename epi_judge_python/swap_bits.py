from test_framework import generic_test


def swap_bits(x, i, j):
    # print(bin(x))
    # print("i:" , i , " and j:" , j)
    # # print(bin(x >> i))
    # # print(bin(x >> j))
    # print(bin((x >> i) & 1))
    # print(bin((x >> j) & 1))
    # print(bin(1 << i))
    # print(bin(1 << j))
    if( x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
