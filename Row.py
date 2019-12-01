import Acts
from Page import Page


class Row:
    rows = 0

    def __init__(self, page: Page):
        self.page = page
        Row.rows += 1
        self.view = None
        self.view = []

    def __getitem__(self, item):
        return self.view[item]

    def __setitem__(self, key, value):
        self.view[key] = value

    def append(self, value):
        self.view.append(value)
