from copy import deepcopy
import heapq

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

def heuristic(board):
    return sum(row.count(0) for row in board)  # total empty cells

def solve_sudoku_astar(initial_board, node_counter):
    heap = []
    heapq.heappush(heap, (heuristic(initial_board), initial_board))
    node_counter[0] = 1

    while heap:
        _, board = heapq.heappop(heap)
        empty = find_empty_cell(board)
        if not empty:
            return board

        row, col = empty
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                new_board = deepcopy(board)
                new_board[row][col] = num
                cost = heuristic(new_board)
                heapq.heappush(heap, (cost, new_board))
                node_counter[0] += 1
    return None
