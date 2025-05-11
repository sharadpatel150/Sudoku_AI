# 🧠 Sudoku Using AI Techniques

This project implements and compares different AI-based search algorithms to solve Sudoku puzzles. It models Sudoku as a **Constraint Satisfaction Problem (CSP)** and evaluates the efficiency of various algorithms based on execution time and nodes explored.

## 📌 Features

- ✅ Load Sudoku puzzles from CSV files
- ✅ Select solver algorithm via CLI
- ✅ Implemented Solvers:
  - Depth-First Search (DFS / Backtracking)
  - Breadth-First Search (BFS)
  - Greedy Search
  - A\* Search
- 📊 Performance metrics:
  - Execution time
  - Nodes explored
- 🧪 Evaluation on multiple difficulty levels
  

---

## 🚀 Getting Started  


### 🔧 Prerequisites

- Python 3.10 and newer.

### 📂 Folder Structure

```bash
sudoku_ai_solver/
├── main.py                         # Entry point with CLI
├── puzzles/                        # Folder with sample .csv puzzles
│   ├── easy1.csv
│   ├── medium1.csv
│   └── ...
├── solver/                         # Folder with AI solvers
│   ├── dfs_solver.py
│   ├── bfs_solver.py
│   ├── greedy_solver.py
│   └── astar_solver.py
├── utils/                          # Utility functions
│   └── board_loader.py
├── README.md
```

## 🧩 Input Format (CSV)
- Each Sudoku puzzle is a .csv file containing 9 rows and 9 columns.
- Use 0 to indicate an empty cell.
- Example:

```bash
5,3,0,0,7,0,0,0,0  
6,0,0,1,9,5,0,0,0  
0,9,8,0,0,0,0,6,0  
...
```

## How It Works
1. Run the script:
```bash
python main.py
```

2. Select the solver:
```bash
Select Solver:
1. DFS
2. BFS
3. Greedy
4. A*
```


## 📊 Evaluation Metrics
- ⏱ Execution Time (seconds)
- 🔁 Nodes Explored (for performance comparison)
- ✅ Solution correctness


## 📚 References
- Norvig, P. (2006). Solving Every Sudoku Puzzle – Used constraint propagation + search.
- [Russell & Norvig. Artificial Intelligence: A Modern Approach (3rd ed.)] – Chapter on CSPs and search strategies.
- History of Sudoku: https://sudoku.com/how-to-play/the-history-of-sudoku/

## ✍️ Author
- Sharadkumar Patel 
- Urvang Patel

## Demo: https://youtu.be/I2dP5b-hZUU
