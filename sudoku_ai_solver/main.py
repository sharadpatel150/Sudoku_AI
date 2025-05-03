import time
from utils.board_loader import load_board_from_csv, print_board
from solver.dfs_solver import solve_sudoku_dfs
from solver.bfs_solver import solve_sudoku_bfs
from solver.greedy_solver import solve_sudoku_greedy
from solver.astar_solver import solve_sudoku_astar

def main():
    file_path = "/Users/ap/Desktop/UNH/AI2025/sudoku_ai_solver/puzzles/medium1.csv"
    board = load_board_from_csv(file_path)

    print("Initial Sudoku Board:")
    print_board(board)

    print("\nSelect Solver:")
    print("1. DFS (Backtracking)")
    print("2. BFS (Breadth-First Search)")
    print("3. Greedy Search (MRV Heuristic)")
    print("4. A* Search (Heuristic)")
    choice = input("Enter choice: ").strip()

    solved_board = None
    node_counter = [0]
    start_time = time.time()

    if choice == "1":
        print("\nSolving using DFS...")
        if solve_sudoku_dfs(board, node_counter):
            solved_board = board
    elif choice == "2":
        print("\nSolving using BFS...")
        if solve_sudoku_bfs(board, node_counter):
            solved_board = board
    elif choice == "3":
        print("\nSolving using Greedy Search...")
        if solve_sudoku_greedy(board, node_counter):
            solved_board = board
    elif choice == "4":
        print("\nSolving using A* Search...")
        solved_board = solve_sudoku_astar(board, node_counter) 
    else:
        print("Invalid choice. Exiting.")
        return

    end_time = time.time()
    elapsed_time = end_time - start_time

    if solved_board:
        print("\nSolved Sudoku Board:")
        print_board(solved_board)
        print(f"\nExecution Time: {elapsed_time:.4f} seconds")
        print(f"Nodes Explored: {node_counter[0]}")
    else:
        print("Solver could not find a solution.")

if __name__ == "__main__":
    main()
