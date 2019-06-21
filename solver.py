class SudokuSolver:

    def __init__(self, board, row=0, column=0):
        self.board = board
        self.row = row
        self.column = column

    def solve(self):
        if not self.is_valid():
            return False

        if self.is_complete():
            return True
        
        self.print_board(self.board)

        for value in range(1, 10):
            new_board = self.board.copy()
            new_board[self.row][self.column] = value

            new_row = self.row
            new_column = self.column + 1

            if new_column >= 9:
                new_row += 1
                new_column = 0

            solver = SudokuSolver(new_board, new_row, new_column)
            
            if solver.solve():
                return True
        
        return False

    def print_board(self, board):
        output = ''
        
        for column in range(0, 9):
            for row in range(0, len(board)):
                if board[row][column] == '':
                    output += '-'
                else:
                    output += str(board[row][column])
            
            output += '\n'
        
        print(output)

    def is_complete(self):
        '''
        Checks there are empty squares
        '''

        # check the board for empty squares
        for row in self.board:
            for item in row:
                if item == '':
                    return False
    
    def is_valid(self):
        '''
        Checks that the current board complies with the rules
        '''
        
        columns = {}
        rows = {}

        for row in range(0, len(self.board)):
            for column in range(0, len(self.board[row])):
                number = self.board[row][column]

                # check for empty space
                if number == '':
                    continue

                # check row is set
                if row not in rows:
                    rows[row] = [number]
                # check for duplicate
                elif number in rows[row]:
                    return False
                # add number to row
                else:
                    rows[row].append(number)

                # check column is set
                if column not in columns:
                    columns[column] = [number]
                # check for duplicate
                elif number in columns[column]:
                    return False
                # add number to column
                else:
                    columns[column].append(number)
        
        return True