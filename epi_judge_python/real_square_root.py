from test_framework import generic_test
import math

def square_root(x: float) -> float:
    left, right = (x, 1.0) if x < 1.0 else (1.0 , x)
    while not math.isclose(left, right):
        mid = 0.5 * ( left + right )
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left 



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
