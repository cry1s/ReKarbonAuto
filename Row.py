import Acts
from tkinter import *


class Row:

    def __init__(self, master, mw):
        self.mw = mw  # MainWindow
        self.master = master
        self.view = []
        self.hard = False

    def __getitem__(self, item):
        return self.view[item]

    def __setitem__(self, key, value):
        self.view[key] = value

    def append(self, value):
        self.view.append(value)

    def grid(self):
        row_at_page = (self.mw.rows.index(self)) % 20
        for i in range(len(self.view)):
            self.view[i].grid(row=row_at_page, column=2*i, sticky='w')

    def grid_remove(self):
        for i in range(len(self.view)):
            self.view[i].grid_remove()

    def grid_option(self):
        row_at_page = (self.mw.rows.index(self)) % 20
        for i in range(len(self.view)):
            self.view[i].grid(row=row_at_page, column=i + 1, sticky='w')

    def update(self):  # grid_remove() + grid(), but more effective
        row_at_page = (self.mw.rows.index(self)) % 20
        for i in range(len(self.view)):
            self.view[i].grid_remove()
            self.view[i].grid(row=row_at_page, column=2*i, sticky='w')

    def to_main(self):
        if self[1].get() == "":
            return ""
        else:
            return self[0].cget("text") + "=" + self[1].get() + ", "
