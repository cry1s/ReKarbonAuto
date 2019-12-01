from tkinter import *
from tkinter import messagebox

import Acts
from Chooser import Chooser
from Row import Row

from Page import Page


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x500')
        self.root.title('KarbonAuto')
        self.root.resizable(1, 0)
        self.pages = [Page(master=self.root)]
        self.current_page = 0
        self.rows = []
        self.numbers = []
        self.root.grid_columnconfigure(0, weight=0)
        self.structure = [
            [Button(self.root, text="Добавить", command=self.new_row), Spinbox(self.root, from_=1, to=1000, width=5)],
            # row 0
            [self.pages[0]],  # row 1
        ]
        self.structure[0][0].grid_configure(row=0, column=0, columnspan=7, sticky='w')
        self.structure[1][0].grid_configure(row=1, column=1)
        self.structure[0][1].grid(row=0, column=2, sticky='w')
        self.structure[0][1].bind('<Return>', lambda event: self.to_page(int(self.structure[0][1].get())-1))
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
        self.pages[self.current_page].close()
        self.pages[-1].show()
        self.current_page += 1

    def to_page(self, page):
        self.pages[self.current_page].close()
        try:
            self.pages[page].show()
            self.current_page = page
        except IndexError:
            messagebox.showerror("Ошибка", "Превышено текущее количество страниц (" + str(len(self.pages)) + ")")
            self.to_page(self.current_page)


a = MainWindow()
