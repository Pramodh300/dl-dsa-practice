#Search an Element in a 2D Matrix (LeetCode 74)
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 16

rows = len(matrix)
cols = len(matrix[0])

left = 0
right = rows * cols - 1

found = False

while left <= right:

    mid = (left + right) // 2

    row = mid // cols
    col = mid % cols

    value = matrix[row][col]

    if value == target:
        found = True
        break

    elif value < target:
        left = mid + 1

    else:
        right = mid - 1

print("Found" if found else "Not Found")



#Return the Position of Target
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

target = 15

rows = len(matrix)
cols = len(matrix[0])

left = 0
right = rows * cols - 1

while left <= right:

    mid = (left + right) // 2

    row = mid // cols
    col = mid % cols

    if matrix[row][col] == target:
        print("Target Found")
        print("Row :", row)
        print("Column :", col)
        break

    elif matrix[row][col] < target:
        left = mid + 1

    else:
        right = mid - 1
else:
    print("Target Not Found")


#Count Comparisons Performed
matrix = [
    [2, 4, 6, 8],
    [10, 12, 14, 16],
    [18, 20, 22, 24]
]

target = 20

rows = len(matrix)
cols = len(matrix[0])

left = 0
right = rows * cols - 1

comparisons = 0

while left <= right:

    comparisons += 1

    mid = (left + right) // 2

    row = mid // cols
    col = mid % cols

    value = matrix[row][col]

    if value == target:
        print("Found")
        print("Comparisons =", comparisons)
        break

    elif value < target:
        left = mid + 1

    else:
        right = mid - 1
else:
    print("Not Found")


#Search Multiple Targets
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

targets = [3, 11, 60, 15]

rows = len(matrix)
cols = len(matrix[0])

for target in targets:

    left = 0
    right = rows * cols - 1

    found = False

    while left <= right:

        mid = (left + right) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            found = True
            break

        elif value < target:
            left = mid + 1

        else:
            right = mid - 1

    if found:
        print(f"{target} -> Found at ({row}, {col})")
    else:
        print(f"{target} -> Not Found")