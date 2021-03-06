import Settings


class Row:

    def __init__(self, master, mw):
        self.mw = mw  # MainWindow
        self.master = master
        self.view = []
        self.hard = False

    def __getitem__(self, item):
        return self.view[item]

    def __setitem__(self, key, value):
        self.view[key] = value

    def append(self, value):
        self.view.append(value)

    def read(self):
        command = ""
        try:
            category = Settings.categories.index(self[0].get())
        except ValueError:
            self.mw.error("void")
            category = 0
        if category == 2:
            command = Settings.commands[2][0].format(self[1].get())
        elif category == 3:
            name = self[1].get()
            if name == Settings.names[3][0]:
                command = "$o"  # flag open cycle
                command += Settings.commands[3][0].format("cycle"+str(self.mw.rows.index(self)), str(self[3].cget("text")[self[3].cget("text").index('=')+1:]))
            else:
                command = "$c"  # flag close cycle
        elif category == 4:
            command = self[1].get()
        elif not Settings.categories[category][0] is None and not category == 3 and not category == 2:
            name = Settings.names[category].index(self[1].get())
            try:
                atts = self[3].cget("text")
            except IndexError:
                atts = ""
            if category == 0 and name == 4:
                command = Settings.commands[category][name].format(atts[atts.index("=")+1:])
            else:
                command = Settings.commands[category][name].format(atts)
        return command

    def grid(self):
        row_at_page = (self.mw.rows.index(self)) % 20
        for i in range(len(self.view)):
            self.view[i].grid(row=row_at_page, column=2*i, sticky='w')

    def grid_remove(self):
        for i in range(len(self.view)):
            self.view[i].grid_remove()

    def grid_option(self):
        row_at_page = (self.mw.rows.index(self)) % 20
        for i in range(len(self.view)):
            self.view[i].grid(row=row_at_page, column=i + 1, sticky='w')

    def update(self):  # grid_remove() + grid(), but more effective
        row_at_page = (self.mw.rows.index(self)) % 20
        for i in range(len(self.view)):
            self.view[i].grid_remove()
            self.view[i].grid(row=row_at_page, column=2*i, sticky='w')

    def to_main(self):
        if self[1].get() == "":
            return ""
        else:
            return self[0].cget("text") + "=" + self[1].get() + ", "
