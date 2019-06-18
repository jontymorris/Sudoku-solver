from window import SodokuWindow
from solver import SodokuSolver


def solver_callback(board, status: bool, message):
    # show board
    print(board)
    print(status)
    print(message)


def window_callback(board):
    # solve the board
    solver = SodokuSolver(board, solver_callback)


# create the window
window = SodokuWindow(window_callback)