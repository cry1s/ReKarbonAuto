from tkinter import *
from tkinter import messagebox

import Acts
from Chooser import Chooser
from Row import Row


class MainWindow:
    def __init__(self):
        # Window setup
        self.root = Tk()
        self.root.geometry('700x500')
        self.root.title('KarbonAuto')
        self.root.resizable(1, 0)
        self.root.grid_columnconfigure(0, weight=0)
        # Variables
        self.pages = 1
        self.current_page = 1
        self.rows = []
        self.numbers = []
        # Window's widget setup
        self.structure = [
            [Button(self.root, text="Добавить", command=self.new_row), Spinbox(self.root, from_=1, to=1000, width=5)],
            # row 0
            [Frame(master=self.root)],  # row 1
            [Label(master=self.root, text="--------------------------------------------")]  # TODO
        ]
        self.structure[0][0].grid_configure(row=0, column=0, columnspan=2, sticky='w')
        self.structure[1][0].grid_configure(row=1, column=1, rowspan=20, columnspan=7)
        self.structure[0][1].grid_configure(row=0, column=2, sticky='w')
        self.structure[2][0].grid_configure(row=21, column=1)
        self.structure[0][1].bind('<Return>', lambda event: self.to_page(int(self.structure[0][1].get())))
        # Window start
        self.root.mainloop()

    def new_row(self):
        self.rows.append(Row(self.structure[1][0]))
        self.pages = (len(self.rows) - 1) // 20 + 1
        if self.pages != self.current_page:
            self.frame_clean()
            self.current_page = self.pages
        row_at_page = (len(self.rows) - 1) % 20
        self.rows[-1].append(Chooser(Acts.categories, [], self.rows[-1]))
        self.rows[-1].grid(row=row_at_page)
        self.numbers.append(Label(master=self.root, text=str(len(self.numbers) + 1)))
        self.numbers[-1].grid(row=row_at_page + 1, column=0)

    def frame_clean(self):
        i = self.current_page
        for k in range(len(self.rows[(i - 1) * 20:i * 20])):
            self.rows[(i - 1) * 20 + k].grid_remove()
            self.numbers[(i - 1) * 20 + k].grid_remove()

    def to_page(self, page):
        self.frame_clean()
        if (page - 1) * 20 > len(self.rows):
            messagebox.showerror("Ошибка", "Превышено текущее количество страниц (" + str(self.pages) + ")")
            self.to_page(self.current_page)
        else:
            for i in range(len(self.rows[(page - 1) * 20:page * 20])):
                self.rows[i + (page - 1) * 20].grid(row=i)
                self.numbers[i + (page - 1) * 20].grid()
                self.current_page = page


a = MainWindow()
