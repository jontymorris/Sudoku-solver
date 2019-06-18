from tkinter import *
from threading import Thread


class SodokuWindow:

    def __init__(self, callback):
        self.callback = callback

        self.root = Tk()
        self.root.title('Sodoku Solver')

        self.grid_entries = []

        # generate the grid
        for row in range(0, 9):
            for column in range(0, 9):
                entry = Entry(self.root)
                entry.place(x=row*30, y=column*30, width=25)
                
                self.grid_entries.append(entry)

        button = Button(self.root, text="Solve!", command=self.solve_click)
        button.place(x=10, y=270)

        self.root.geometry('280x300')
        self.root.mainloop()
    
    def solve_click(self):
        grid = []
        current_row = []

        for item in self.grid_entries:
            current_row.append(item.get())

            if len(current_row) >= 3:
                grid.append(current_row)
                current_row = []
        
        self.callback(grid)