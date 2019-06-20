from tkinter import *
from threading import Thread


class SudokuWindow:

    def __init__(self, callback):
        self.callback = callback

        self.root = Tk()
        self.root.title('Sudoku Solver')
        self.root.configure(background='#C7C7C7')
        self.root.resizable(False, False)

        self.grid_entries = []

        # generate the grid
        row_offset = 0
        column_offset = 0
        for row in range(0, 9):
            column_offset = 0

            if row % 3 == 0:
                row_offset += 10

            for column in range(0, 9):
                if column % 3 == 0:
                    column_offset += 10

                entry = Entry(self.root)
                entry.place(x=(row*30)+row_offset, y=(column*30)+column_offset, width=25)
                
                self.grid_entries.append(entry)

        button = Button(self.root, text="Solve!", command=self.solve_click)
        button.place(x=10, y=300)

        self.root.geometry('305x330')
        self.root.mainloop()
    
    def solve_click(self):
        grid = []
        current_row = []

        for item in self.grid_entries:
            current_row.append(item.get())

            if len(current_row) >= 9:
                grid.append(current_row)
                current_row = []
        
        self.callback(grid)