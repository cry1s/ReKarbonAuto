import time
from tkinter import Tk, Label, Entry, Button

import pyautogui

from Row import Row


class OptionWindow(Tk):
    def __init__(self, attributes, row):
        super().__init__()
        self.title("Опции")
        self.iconbitmap(r'res\ico.ico')
        self.resizable(False, False)
        self.row = row
        self.attributes = attributes.split(', ')
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
        xy = pyautogui.position()
        self.rows[-1].append(Label(master=self, text="x=" + str(xy.x) + ", y=" + str(xy.y)))
        self.rows[-1][-1].bind("<Motion>", lambda *args: self.xyxy())
        self.rows[-1].grid_option()

    def to_main(self):
        self.row.grid_remove()
        self.row.view = self.row.view[:3]
        text = ""
        for i in range(len(self.rows) - 1):
            text += self.rows[i].to_main()
        text = text[:-2]
        self.row.append(Label(master=self.row.master, text=text))
        self.row.update()
        self.destroy()

    def xyxy(self):
        xy = pyautogui.position()
        self.rows[-1].grid_remove()
        self.rows[-1][-1] = Label(master=self, text="x=" + str(xy.x) + ", y=" + str(xy.y))
        self.rows[-1][-1].bind("<Motion>", lambda *args: self.xyxy())
        self.rows[-1].grid_option()
        time.sleep(0.3)
