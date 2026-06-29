#Spiral order
def spiral_order(matrix):
    result = []

    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Top Row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Right Column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Bottom Row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Left Column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(spiral_order(matrix))



#90 degree rotation
def rotate(matrix):
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

    return matrix


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rotate(matrix)

for row in matrix:
    print(row)