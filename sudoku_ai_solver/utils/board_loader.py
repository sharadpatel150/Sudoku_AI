import csv

def load_board_from_csv(file_path):
    board = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            board.append([int(cell) for cell in row])
    return board

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
