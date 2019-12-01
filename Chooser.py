from tkinter import ttk

import Row


class Chooser(ttk.Combobox):
    def __init__(self, to_choose_list: list, to_do_list: list, row: Row, **kw):
        super().__init__(row.page, value=to_choose_list, state='readonly', width=15, **kw)
        self.to_do = to_do_list
        self.row = row.view
