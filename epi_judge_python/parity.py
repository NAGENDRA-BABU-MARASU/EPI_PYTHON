from test_framework import generic_test


def parity(x: int) -> int:
    # result = 0
    # while x:
    #     result = result ^ 1
    #     x = (x & (x-1))
    #
    # return result
    # MASK_SIZE = 16
    # BIT_MASK = 0xFFFF
    # return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^ PRECOMPUTED_PARITY[x >> (2 * MASK_SIZE) & BIT_MASK]
    #         ^ PRECOMPUTED_PARITY[x >> MASK_SIZE & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK]  )
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
