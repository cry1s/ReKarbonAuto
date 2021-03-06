from tkinter import ttk, Tk, Spinbox, Label, Entry, Button
import Settings
from OptionWindow import OptionWindow
from Row import Row


class Chooser(ttk.Combobox):
    def __init__(self, to_choose_list: list = Settings.categories, row: Row = None, **kw):
        super().__init__(master=row.master, value=to_choose_list, state='readonly', width=15, **kw)
        self.row = row
        self.bind('<<ComboboxSelected>>', lambda *args: self.create())

    def create(self):
        choosed = self.get()
        if choosed == "":
            return
        column = self.row.view.index(self)
        self.row.grid_remove()
        self.row.view = self.row.view[:column + 1]
        if column == 0:
            category = Settings.categories.index(choosed)
            if Settings.names[category][0]:
                self.row.hard = False
                self.row.append(Chooser(Settings.names[category], self.row))
                self.row[-1].grid_configure(columnspan=2)
                self.row.update()
            else:
                self.row.hard = True
                self.create_hard(choosed)
                self.row.update()
        elif column == 1:
            category = Settings.categories.index(self.row[0].get())
            name = Settings.names[category].index(choosed)
            if not (category == 2 and name == 1):
                self.row.append(Label(self.row.master, image=self.row.mw.img1))
                self.row[-1].bind("<Button-1>", lambda *args: OptionWindow(Settings.attributes[category][name], self.row).mainloop())
                self.row.update()

    def create_hard(self, choosed):
        if choosed == "Строка Python":
            self.row.append(Entry(self.row.master, width=40))
            self.row[-1].grid_configure(columnspan=7)
        elif choosed == "Ждать":
            self.row.append(Spinbox(self.row.master, from_=0.01, to=1000000, width=8))
            self.row.append(Label(self.row.master, text="секунд"))
