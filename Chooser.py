import Row


class Chooser:
    def __init__(self, tochooselist: set, todolist: set, row: Row):
        self.todo = todolist
        self.tochoose = tochooselist
        self.row = row.view

    def grid(self):
        pass