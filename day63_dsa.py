#Brute Force Code
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

k = 2

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows-k+1):

    for j in range(cols-k+1):

        total = 0

        for r in range(i, i+k):

            for c in range(j, j+k):

                total += matrix[r][c]

        print(total)
        
        

#Maximum Sum 3 x 3 Window
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,1,2,3],
    [4,5,6,7]
]

k = 3

rows = len(matrix)
cols = len(matrix[0])

maximum = float("-inf")

for i in range(rows-k+1):

    for j in range(cols-k+1):

        total = 0

        for r in range(i, i+k):

            for c in range(j, j+k):

                total += matrix[r][c]

        maximum = max(maximum, total)

print(maximum)



#Find The Average Brightness Of Every 3 x 3 Window
matrix = [
    [10, 20, 30, 40],
    [20, 30, 40, 50],
    [30, 40, 50, 60],
    [40, 50, 60, 70]
]

k = 3

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows - k + 1):

    for j in range(cols - k + 1):

        total = 0

        for r in range(i, i + k):

            for c in range(j, j + k):

                total += matrix[r][c]

        average = total / (k * k)

        print(f"Window ({i},{j}) Average = {average:.2f}")



#Find The Minimum Sum k x k Submatrix
matrix = [
    [5, 8, 2, 6],
    [1, 9, 4, 7],
    [3, 2, 6, 8],
    [4, 1, 5, 9]
]

k = 2

rows = len(matrix)
cols = len(matrix[0])

min_sum = float('inf')
position = (0, 0)

for i in range(rows - k + 1):

    for j in range(cols - k + 1):

        current_sum = 0

        for r in range(i, i + k):

            for c in range(j, j + k):

                current_sum += matrix[r][c]

        print(f"Window ({i},{j}) = {current_sum}")

        if current_sum < min_sum:
            min_sum = current_sum
            position = (i, j)

print("\nMinimum Sum =", min_sum)
print("Top-left position =", position)

print("\nMinimum Sum Submatrix:")

for r in range(position[0], position[0] + k):
    for c in range(position[1], position[1] + k):
        print(matrix[r][c], end=" ")
    print()