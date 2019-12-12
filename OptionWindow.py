from tkinter import Tk, Label

from Row import Row


class OptionWindow(Tk):
    def __init__(self, attributes):
        super().__init__(screenName="Опции")
        self.attributes = attributes.split(', ')
        print(self.attributes)
        self.rows = []
        for i in range(len(attributes) // 2):
            self.rows.append(Row(master=self, mw=self))
            try:
                self.rows[-1].append(Label(text=self.attributes[2 * i][:self.attributes[2 * i].index("=")]))
            except ValueError:
                self.rows[-1].append(Label(text=self.attributes[2 * i]))
            try:
                self.rows[-1].append(Label(text=self.attributes[2 * i + 1][:self.attributes[2 * i + 1].index("=")]))
            except ValueError:
                self.rows[-1].append(Label(text=self.attributes[2 * i + 1]))
            except IndexError:
                self.rows[-1].grid()
                return
            self.rows[-1].grid()
