from Chooser import Chooser

class Row:
    rows = 0
    def __init__(self, view: set):
        Row.rows += 1
        self.view = [Chooser()]
