import Acts
from tkinter import *

class Row:
    rows = 0

    def __init__(self, master):
        self.master = master
        Row.rows += 1
        self.view = []

    def __getitem__(self, item):
        return self.view[item]

    def __setitem__(self, key, value):
        self.view[key] = value

    def append(self, value):
        self.view.append(value)

    def grid(self, row):
        for i in range(len(self.view)):
            self.view[i].grid(row=row, column=i+1, sticky='w')

    def grid_remove(self):
        for i in range(len(self.view)):
            self.view[i].grid_remove()

    def update(self, row):
        self.grid_remove()
        self.grid(row)
