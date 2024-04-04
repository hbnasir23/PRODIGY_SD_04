import tkinter as tk
from tkinter import messagebox

def is_valid_move(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def create_sudoku_grid(root):
    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            cell = tk.Entry(root, width=3, font=('Arial', 16), justify='center', highlightbackground="black", highlightthickness=1)
            cell.grid(row=i, column=j, padx=1, pady=1)
            row.append(cell)
            if (i+1) % 3 == 0 and (j+1) % 3 == 0:
                cell.grid(padx=(1, 10), pady=(1, 10))
            elif (i+1) % 3 == 0:
                cell.grid(padx=(1, 1), pady=(1, 10))
            elif (j+1) % 3 == 0:
                cell.grid(padx=(1, 10), pady=(1, 1))
            else:
                cell.grid(padx=(1, 1), pady=(1, 1))
        cells.append(row)
    return cells

def solve():
    global cells
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = cells[i][j].get()
            if value:
                try:
                    num = int(value)
                    if num < 1 or num > 9:
                        raise ValueError("Invalid value")
                    if not is_valid_move(board, i, j, num):
                        raise ValueError("Invalid move")
                    board[i][j] = num
                except ValueError:
                    messagebox.showinfo("Error", f"Invalid value at cell ({i+1}, {j+1})")
                    return

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                cells[i][j].delete(0, tk.END)
                cells[i][j].insert(0, str(board[i][j]))
                cells[i][j].config(state="disabled", disabledbackground="#f0f0f0", disabledforeground="black", font=('Arial', 16, 'bold'))
    else:
        messagebox.showinfo("Error", "No solution exists for the Sudoku puzzle.")

def new_game():
    global cells
    for i in range(9):
        for j in range(9):
            cells[i][j].config(state="normal")
            cells[i][j].delete(0, tk.END)

root = tk.Tk()
root.title("Sudoku Solver")
root.configure(background="teal")

cells = create_sudoku_grid(root)

solve_button = tk.Button(root, text="Solve Sudoku", command=solve, font=('Arial', 14, 'bold'), bg="#4CAF50", fg="white", padx=10, pady=5)
solve_button.grid(row=9, column=0, columnspan=9, pady=(10, 5))

new_game_button = tk.Button(root, text="New Game", command=new_game, font=('Arial', 14, 'bold'), bg="#FFC107", fg="black", padx=10, pady=5)
new_game_button.grid(row=10, column=0, columnspan=9, pady=(5, 10))

root.mainloop()
