def dfs(grid, row, col, visited):

    rows = len(grid)
    cols = len(grid[0])

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return

    if grid[row][col] == 0:
        return

    if visited[row][col]:
        return

    visited[row][col] = True

    print(f"Visited: ({row}, {col})")

    dfs(grid, row - 1, col, visited)
    dfs(grid, row + 1, col, visited)
    dfs(grid, row, col - 1, visited)
    dfs(grid, row, col + 1, visited)


grid = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 1, 1]
]

rows = len(grid)
cols = len(grid[0])

visited = [[False] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1 and not visited[i][j]:
            print(f"\nStarting DFS from ({i}, {j})")
            dfs(grid, i, j, visited)



#BFS Code
from collections import deque

def bfs(grid, row, col):

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    queue = deque()

    queue.append((row, col))
    visited[row][col] = True

    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    while queue:

        r, c = queue.popleft()

        print("Visited:", r, c)

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                not visited[nr][nc] and
                grid[nr][nc] == 1
            ):

                visited[nr][nc] = True
                queue.append((nr, nc))


grid = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 1, 1]
]

bfs(grid, 0, 0)


#Number of Islands(DFS)
def dfs(grid, row, col):

    rows = len(grid)
    cols = len(grid[0])

    # Check boundaries
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return

    # Water or already visited
    if grid[row][col] == "0":
        return

    # Mark as visited
    grid[row][col] = "0"

    # Visit all 4 directions
    dfs(grid, row - 1, col)   # Up
    dfs(grid, row + 1, col)   # Down
    dfs(grid, row, col - 1)   # Left
    dfs(grid, row, col + 1)   # Right


def num_islands(grid):

    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == "1":
                islands += 1
                dfs(grid, i, j)

    return islands


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print("Number of Islands:", num_islands(grid))



#Flood Fill(BFS)
from collections import deque

def flood_fill(image, sr, sc, new_color):

    rows = len(image)
    cols = len(image[0])

    original = image[sr][sc]

    if original == new_color:
        return image

    queue = deque()
    queue.append((sr, sc))

    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    image[sr][sc] = new_color

    while queue:

        r, c = queue.popleft()

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                image[nr][nc] == original
            ):

                image[nr][nc] = new_color
                queue.append((nr, nc))

    return image


image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

result = flood_fill(image, 1, 1, 2)

print("Flood Filled Image:")

for row in result:
    print(row)