from window import SudokuWindow
from solver import SudokuSolver


def solver_callback(board, status: bool, message):
    # show board
    print(board)
    print(status)
    print(message)


def window_callback(board):
    # solve the board
    solver = SudokuSolver(board, solver_callback)


# create the window
window = SudokuWindow(window_callback)