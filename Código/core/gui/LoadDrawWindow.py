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

class LoadDrawWindow(tk.Frame):
    def __init__(self,master,parent, user_id, user_role, draw_id= {}):
        super().__init__(master)
        self.parent = parent
        self.master = master
        self.userID = user_id
        self.userRole = user_role
        self.buildWindow(draw_id)

    """
        Creo la ventana de carga    
    """
    def buildWindow(self, new_id):
        self.centerWindow()
        if self.userRole == 1:
            self.columns = ("id","drawing", "user")
        else:
            self.columns = ("id","drawing")
        self.treeview = ttk.Treeview(self.master, columns = self.columns, selectmode= "browse", show="headings")
        # Evento que se dispara cada vez que doy click en un item
        self.treeview.tag_bind("draw", "<<TreeviewSelect>>", self.item_selected)
        if self.userRole == 1:
            self.treeview.column("id", width=40, stretch=False, anchor=tk.CENTER)
            self.treeview.column("drawing", width=130, stretch=False, anchor=tk.CENTER)
            self.treeview.column("user", width=130, stretch=False, anchor=tk.CENTER)
            self.treeview.heading("id", text = "id")
            self.treeview.heading("drawing", text = "Drawing Name")
            self.treeview.heading("user", text = "User")
        else:
            self.treeview.column("id", width=40, stretch=False, anchor=tk.CENTER)
            self.treeview.column("drawing", width=270, stretch=False, anchor=tk.CENTER)
            self.treeview.heading("id", text = "id")
            self.treeview.heading("drawing", text = "Drawing Name")
        self.getDrawList()
        self.treeview.pack()

        """
            Agrego al ultimo parametro de la clase el contenido del dibujo desencriptado desde la base de datos y 
            luego cierro la ventana
        """
        def loadDraw():
            res = engine.call('sp_getOneDrawing', values = [int(self.drawSelected)])
            for value in res:
                new_id['content'] = em.decryptDraw(value.fetchone()[0])
            self.master.destroy()

        openButton = tk.Button(self.master, text="Load", command=loadDraw)
        openButton.pack()

    # Obtengo el id del item y despues el id que tiene en la base
    def item_selected(self, event):
        eid = self.treeview.selection()[0]
        self.drawSelected = self.treeview.set(eid, "id")
    
    """
        Método para obtener la lista de todos los dibujos o de los dibujos de un usuario, dependiendo de quien se loguee
    """
    def getDrawList(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        self.draws = dm.getDraws(self.userID, self.userRole)
        for draw in self.draws:
            if self.userRole == 1:
                self.treeview.insert("", "end", value=(draw[0], draw[1], draw[2]), tags=("draw"))
            else:
                self.treeview.insert("", "end", value=(draw[0], draw[1]), tags=("draw"))


    def centerWindow(self):
        w = 300
        h = 250

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))