# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import scrolledtext as st, messagebox
from tkinter import ttk

from ..modules.encrypt.EncryptManager import EncryptManager
from ..modules.database.MySQLEngine import MySQLEngine
from ..modules.draw.DrawingManager import DrawingManager

engine = MySQLEngine()
em = EncryptManager()
dm = DrawingManager()

class SaveDrawWindow(tk.Frame):
    def __init__(self,master, parent, user_id, user_role, drawing, draw_name = "", draw_id = 0):
        super().__init__(master)
        self.userID = user_id
        self.userRole = user_role
        self.draw_Name = draw_name
        self.drawId = draw_id
        self.drawing  = drawing
        self.master = master
        self.buildWindow()

    """
        Construyo la ventana
    """
    def buildWindow(self):
        self.centerWindow()
        if self.userRole == 1:
            self.columns = ("drawing", "user")
        else:
            self.columns = ("drawing")
        self.treeview = ttk.Treeview(self.master, columns = self.columns, selectmode= "browse")
        if self.userRole == 1:
            self.treeview.column("#0", width=40, stretch=False, anchor=tk.CENTER)
            self.treeview.column("drawing", width=130, stretch=False, anchor=tk.CENTER)
            self.treeview.column("user", width=130, stretch=False, anchor=tk.CENTER)
            self.treeview.heading("#0", text = "id")
            self.treeview.heading("drawing", text = "Drawing Name")
            self.treeview.heading("user", text = "User")
        else:
            self.treeview.column("#0", width=40, stretch=False, anchor=tk.CENTER)
            self.treeview.column("drawing", width=270, stretch=False, anchor=tk.CENTER)
            self.treeview.heading("#0", text = "id")
            self.treeview.heading("drawing", text = "Drawing Name")
        self.getDrawList()
        self.treeview.pack()
        self.drawName = tk.Entry(self.master)
        if self.draw_Name != "":
            self.drawName.insert(0,self.draw_Name)
        self.drawName.pack()
        self.drawName.focus_set()
        openButton = tk.Button(self.master, text="Save", command=self.saveDraw)
        openButton.pack()

    """
        Guardo el dibujo, si todo salio bien muestro el mensaje de guardao y cierro la ventana
    """
    def saveDraw(self):
        name = self.drawName.get()
        if len(name) < 4:
            messagebox.showerror("Error", "Name too short")
        elif self.draw_Name != "":
            res = engine.call('sp_updateDrawing', 'insert', [self.drawId, name, em.encryptDraw(self.drawing)])
            if res:
                messagebox.showinfo("Done!","Draw modified!", parent=self)
                self.master.destroy()
        else:
            res = engine.call('sp_addDrawing', 'insert', [self.userID, name, em.encryptDraw(self.drawing)])
            if res:
                messagebox.showinfo("Done!","Draw added!", parent=self)
                self.master.destroy()

    """
        Obteniendo lista de dibujos
    """
    def getDrawList(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        self.draws = dm.getDraws(self.userID, self.userRole)
        for draw in self.draws:
            if self.userRole == 1:
                self.treeview.insert("", "end", text=draw[0], value=(draw[1], draw[2]))
            else:
                self.treeview.insert("", "end", text=draw[0], value=(draw[1]))


    def centerWindow(self):
        w = 310
        h = 290

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))