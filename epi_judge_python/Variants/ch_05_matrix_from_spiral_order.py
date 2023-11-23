def generate_spiral_order(square_matrix):
    if not square_matrix:
        return []

    rows, cols = len(square_matrix) , len(square_matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    result = []
    while len(result) < rows * cols:
        for i in range(left, right+1):
            result.append(square_matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(square_matrix[i][right])

        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(square_matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom , top-1, -1):
                result.append(square_matrix[i][left])
            left += 1

    return result

print(generate_spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

def get_matrix_from_d_spiral_order(dimension):
    result_matrix = [[0 for j in range(dimension)] for i in range(dimension) ]
    startRow = 0
    endRow = len(result_matrix) -1
    startCol = 0
    endCol = len(result_matrix) - 1

    currentNumber = 1
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result_matrix[startRow][col] = currentNumber
            currentNumber += 1

        for row in range(startRow + 1, endRow + 1):
            result_matrix[row][endCol] = currentNumber
            currentNumber += 1

        for col in reversed(range(startCol, endCol)):
            result_matrix[endRow][col] = currentNumber
            currentNumber += 1

        for row in reversed(range(startRow + 1, endRow )):
            result_matrix[row][startCol] = currentNumber
            currentNumber += 1

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result_matrix

print(get_matrix_from_d_spiral_order(2))