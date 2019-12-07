from tkinter import ttk, Tk

import Row


class Chooser(ttk.Combobox):
    # TODO chooser
    def __init__(self, to_choose_list: list, to_do_list: list, row: Row, **kw):
        super().__init__(master=row.master, value=to_choose_list, state='readonly', width=15, **kw)
        self.to_do = to_do_list
        self.row = row.view
