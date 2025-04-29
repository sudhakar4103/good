def solve_nqueens(n):
    solutions = []
    board = [-1] * n  # board[i] = column of queen in row i

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def backtrack(row=0):
        if row == n:
            solutions.append(board.copy())
            return True  # stop at first solution
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
        return False

    backtrack()
    return solutions[0] if solutions else None

if __name__ == '__main__':
    n = int(input('N (queens): '))
    sol = solve_nqueens(n)
    if sol:
        print('One solution (row:col):', list(enumerate(sol)))
    else:
        print('No solution')
