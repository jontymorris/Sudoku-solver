from window import SudokuWindow
from solver import SudokuSolver


def solver_callback(board, status: bool, message):
    # show board
    print(board)
    print(status)
    print(message)


def window_callback(board):
    print('Now trying to solve...')

    # solve the board
    solver = SudokuSolver(board)
    #print('is valid:', solver.is_valid())
    print(solver.solve())

    print('It finished :(')


# create the window
window = SudokuWindow(window_callback)