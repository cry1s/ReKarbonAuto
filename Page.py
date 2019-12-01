from tkinter import Frame


class Page(Frame):
    pages = 0
    rows = 20

    def __init__(self, **kw):
        super().__init__(**kw)
        Page.pages += 1
        self.number = Page.pages

    def close(self):
        self.grid_remove()

    def show(self):
        self.grid(row=1, column=1)

    @staticmethod
    def minus():
        Page.pages -= 1
