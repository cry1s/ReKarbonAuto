import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

import pyautogui

import Settings
from Chooser import Chooser
from Row import Row
from PIL import ImageTk, Image


class MainWindow:
    def __init__(self):
        # Window setup
        self.filename = None
        self.root = Tk()
        self.root.geometry('700x500')
        self.root.title('KarbonAuto')
        self.root.resizable(1, 0)
        self.root.grid_columnconfigure(0, weight=0)
        # Variables
        self.pages = 1
        self.current_page = 1
        self.rows = []
        self.numbers = []
        self.img1 = ImageTk.PhotoImage(Image.open("res/western.jpg"))
        # Window's widgets setup
        self.structure = [
            [Button(self.root, text="Добавить", command=self.new_row),  # row 0
             Button(self.root, text="Сохранить как", command=self.coding),
             Button(self.root, text="Справка",
                    command=lambda *args: messagebox.showinfo("Справка по клавишам", pyautogui.KEY_NAMES)),
             Spinbox(self.root, from_=1, to=1000, width=5)],
            [Frame(master=self.root)],  # row 1
            [Label(master=self.root, text="TODO")]
        ]
        self.structure[0][0].grid_configure(row=0, column=0, columnspan=2, sticky='w')
        self.structure[1][0].grid_configure(row=1, column=1, rowspan=20, columnspan=9)
        self.structure[0][1].grid_configure(row=0, column=2, sticky='w')
        self.structure[0][2].grid_configure(row=0, column=3, sticky='w')
        self.structure[0][2].grid_configure(row=0, column=4, sticky='w')
        self.structure[2][0].grid_configure(row=21, column=1)
        self.structure[0][1].bind('<Return>', lambda event: self.to_page(int(self.structure[0][1].get())))
        # Window start
        self.root.mainloop()

    def new_row(self):
        if self.current_page != self.pages:
            self.to_page(self.pages)
        self.rows.append(Row(self.structure[1][0], self))
        self.pages = (len(self.rows) - 1) // 20 + 1
        if self.pages != self.current_page:
            self.frame_clean()
            self.current_page = self.pages
        row_at_page = (len(self.rows) - 1) % 20
        self.rows[-1].append(Chooser(Settings.categories, self.rows[-1]))
        self.rows[-1].grid()
        self.numbers.append(Label(master=self.root, text=str(len(self.numbers) + 1)))
        self.numbers[-1].grid(row=row_at_page + 1, column=0)

    def frame_clean(self):
        i = self.current_page
        for k in range(len(self.rows[(i - 1) * 20:i * 20])):
            self.rows[(i - 1) * 20 + k].grid_remove()
            self.numbers[(i - 1) * 20 + k].grid_remove()

    def to_page(self, page):
        if page <= 0:
            messagebox.showerror("Ошибка", "Некорректное число")
        elif (page - 1) * 20 >= len(self.rows) and page != 1:
            messagebox.showerror("Ошибка", "Превышено текущее количество страниц (" + str(self.pages) + ")")
        else:
            self.frame_clean()
            for i in range(len(self.rows[(page - 1) * 20:page * 20])):
                self.rows[i + (page - 1) * 20].grid()
                self.numbers[i + (page - 1) * 20].grid()
                self.current_page = page

    def coding(self):
        # noinspection PyAttributeOutsideInit
        self.file_name = fd.asksaveasfilename(filetypes=(("Python files", "*.py"),))
        if self.file_name[-3:].lower != ".py":
            self.file_name += ".py"
        f = open(self.file_name, 'w')
        s = ""
        for i in range(len(Settings.imports)):
            s += Settings.imports[i] + "\n"
        s += "\n"
        spaces = ""
        for i in range(len(self.rows)):
            readed = self.rows[i].read()
            if readed[0] == "$":
                if readed[1] == "o":
                    spaces += " "
                elif readed[2] == "c":
                    if len(spaces) == 0:
                        self.error("spaces")
                    else:
                        spaces = (len(spaces) - 1) * " "
            else:
                s += spaces * 4 + readed + "\n"
        f.write(s)
        f.close()

    def error(self, error):
        pass


a = MainWindow()
