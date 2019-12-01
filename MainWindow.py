from tkinter import *

import Acts
from Chooser import Chooser
from Row import Row

from Page import Page


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x500')
        self.root.title('KarbonAuto')
        self.root.resizable(0, 0)
        self.pages = [Page(master=self.root)]
        self.rows = []
        self.numbers = []
        self.root.grid_columnconfigure(0, weight=0)
        self.structure = [
            [Button(self.root, text="Добавить", command=self.new_row)],  # row 0
            [self.pages[0]],  # row = 1
        ]
        self.structure[0][0].grid_configure(row=0, column=0, columnspan=2)
        self.structure[1][0].grid_configure(row=1, column=1)

        self.root.mainloop()

    def new_row(self):
        page = len(self.rows) // 20
        if page - len(self.pages) + 1 == 1:
            self.new_page()
        row_at_page = len(self.rows) % 20
        self.rows.append(Row(self.pages[page]))
        self.rows[-1].append(Chooser(Acts.categories, [], self.rows[-1]))
        self.numbers.append(Label(self.pages[page], text=Row.rows))
        self.rows[-1][0].grid(row=row_at_page, column=1)
        self.numbers[-1].grid(row=row_at_page, column=0)

    def new_page(self):
        self.pages.append(Page(master=self.root))
        self.pages[-2].close()
        self.pages[-1].show()


a = MainWindow()
