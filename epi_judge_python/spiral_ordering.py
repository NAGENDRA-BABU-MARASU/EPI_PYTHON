from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:


    spiral_order = []
    startRow, endRow = 0, len(square_matrix) - 1
    startCol, endCol = 0, len(square_matrix) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol +1):
            spiral_order.append(square_matrix[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            spiral_order.append(square_matrix[row][endCol])

        for col in reversed(range(startCol, endCol)):
            spiral_order.append(square_matrix[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            spiral_order.append(square_matrix[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return spiral_order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
