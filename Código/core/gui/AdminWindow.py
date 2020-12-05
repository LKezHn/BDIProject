import tkinter as tk
from .PyList import PyList

class AdminWindow(tk.Frame):

    def __init__(self,master,parent):
        super().__init__(master)
        self.parent = parent
        self.master = master
        self.buildWindow()

    def buildWindow(self):
        self.master.title('Admin Window')
        self.master.geometry('500x500')
        self.master.resizable(width=0, height=0)
        self.master.transient(master=self.parent)
        self.master.focus_set()
        self.master.grab_set()
