from tkinter import Tk, Label, Entry, Button

from Row import Row


class OptionWindow(Tk):
    def __init__(self, attributes, chooser):
        super().__init__()
        self.title("Опции")
        self.chooser = chooser
        self.attributes = attributes.split(', ')
        print(self.attributes)
        self.rows = []
        for i in range(len(self.attributes)):
            self.rows.append(Row(master=self, mw=self))
            try:
                self.rows[-1].append(Label(self, text=self.attributes[i][:self.attributes[i].index("=")]))
            except ValueError:
                self.rows[-1].append(Label(self, text=self.attributes[i]))
            self.rows[-1].append(Entry(self))
            self.rows[-1].grid_option()
        self.rows.append(Row(master=self, mw=self))
        self.rows[-1].append(Button(master=self, text="Отмена", command=lambda *args: self.destroy()))
        self.rows[-1].append(Button(master=self, text="Принять", command=lambda *args: self.to_main()))
        self.rows[-1].grid_option()

    def to_main(self):
        column = self.row.view.index(self.chooser) + 2
        self.row.grid_remove()
        self.row.view = self.row.view[:column + 1]
        self.row.append(Label(text="TODO"))  # TODO stop
