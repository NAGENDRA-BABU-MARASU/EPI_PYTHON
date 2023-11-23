from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    left = 0
    right = len(square_matrix) - 1
    while left < right:
        for i in range(right - left):
            top = left
            bottom = right

            topLeft = square_matrix[top][left + i]
            square_matrix[top][left + i] = square_matrix[bottom - i][left]
            square_matrix[bottom - i][left] = square_matrix[bottom][right - i]
            square_matrix[bottom][right - i] = square_matrix[top + i][right]
            square_matrix[top + i][left] = topLeft

        left += 1
        right -= 1

        


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
