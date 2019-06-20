class SudokuSolver:

    def __init__(self, board, callback):
        self.board = board
        self.callback = callback

        print('Is complete:', self.is_complete())
        print('Is valid:', self.is_valid())

    def solve(self):
        pass

    def is_complete(self):
        '''
        Checks there are no empty squares and the board is valid
        '''

        # check the board for empty squares
        for row in self.board:
            for item in row:
                if item == '':
                    return False

        # return if the board is valid
        return self.is_valid()
    
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