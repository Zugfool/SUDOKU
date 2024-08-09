import random; import time
#whilst creating sudoku

def pick(take):
    RANDOM = random.choice(take)
    return RANDOM

def BOX(x):
    if x<=2:     check = [0,3]
    elif x>=6:   check = [6,9]
    else:          check = [3,6]
    return check

def hardness(desire):
    if desire == "Easy":     amount = 30; rep = 2
    elif desire == "Normal": amount = 27; rep = 2
    elif desire == "Hard":   amount = 24; rep = 2
    elif desire == "Very hard":   amount = 21; rep =1 
    elif desire == "Impossible":  amount = 18; rep=1
    return amount, rep

#whilst solving sudoku

start_time = time.time()
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                end_time = time.time()
                execution_time = end_time - start_time
                return True,execution_time
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid_move(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True