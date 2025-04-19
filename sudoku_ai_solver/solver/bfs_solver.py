from copy import deepcopy
from collections import deque

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

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku_bfs(initial_board, node_counter):
    queue = deque()
    queue.append(initial_board)
    node_counter[0] = 1  # initial state

    while queue:
        board = queue.popleft()
        empty = find_empty_cell(board)
        if not empty:
            return board  # Solved!

        row, col = empty
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                new_board = deepcopy(board)
                new_board[row][col] = num
                queue.append(new_board)
                node_counter[0] += 1  # each new board state is a node

    return None
