#Basic Matrix Traversal
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


rows=len(matrix)

cols=len(matrix[0])


for r in range(rows):

    for c in range(cols):

        print(matrix[r][c])


#Boundary Checking
grid=[
[1,2,3],
[4,5,6],
[7,8,9]
]


directions=[
(-1,0),
(1,0),
(0,-1),
(0,1)
]


r=1
c=1


for dr,dc in directions:


    nr=r+dr

    nc=c+dc


    if (
        nr>=0 and nr<len(grid)
        and
        nc>=0 and nc<len(grid[0])
    ):

        print(
        grid[nr][nc]
        )