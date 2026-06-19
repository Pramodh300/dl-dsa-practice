#N Queens Problem
def solveNQueens(n):
    board = [["." for _ in range(n)] for _ in range(n)]

    cols = set()
    diag1 = set()   # row - col
    diag2 = set()   # row + col

    result = []

    def backtrack(row):

        # Base case
        if row == n:
            solution = ["".join(r) for r in board]
            result.append(solution)
            return

        # Try every column
        for col in range(n):

            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place Queen
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # Explore
            backtrack(row + 1)

            # Backtrack
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


answers = solveNQueens(4)

for solution in answers:
    for row in solution:
        print(row)
    print()


#Sudoku Solver
def solveSudoku(board):

    def is_valid(row, col, num):

        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check 3x3 box
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrack():

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":

                    for num in map(str, range(1, 10)):

                        if is_valid(row, col, num):

                            board[row][col] = num

                            if backtrack():
                                return True

                            # Backtrack
                            board[row][col] = "."

                    return False

        return True

    backtrack()