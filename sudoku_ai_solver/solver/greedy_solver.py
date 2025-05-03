from copy import deepcopy

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_mrv_cell(board):
    min_options = 10
    best_cell = None

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                options = [num for num in range(1, 10) if is_valid(board, row, col, num)]
                if len(options) < min_options:
                    min_options = len(options)
                    best_cell = (row, col, options)
    return best_cell

def solve_sudoku_greedy(board, node_counter):
    empty = find_mrv_cell(board)
    if not empty:
        return True

    row, col, options = empty
    for num in options:
        if is_valid(board, row, col, num):
            board[row][col] = num
            node_counter[0] += 1
            if solve_sudoku_greedy(board, node_counter):
                return True
            board[row][col] = 0  # backtrack
    return False
