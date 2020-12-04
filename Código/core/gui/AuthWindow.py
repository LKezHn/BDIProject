# -*- coding: utf-8 -*-

import tkinter as tk, re
from tkinter import messagebox
from ..auth.AuthManager import AuthManager

am = AuthManager()
"""
    Clase encargada de crear la ventana de autenticación/login de usuarios.
    @author lemartinezm@unah.hn
    @version 1.0.0
    @date 2020/12/01
"""
class AuthWindow(tk.Frame):
    def __init__(self, master, parent, user = {}):
        super().__init__(master)
        self.parent = parent
        self.master = master
        self.buildWindow(user)

    """
        Método encargado de cargar los componentes de la venta de autenticación.
        @param user Es el diccionario que sirve para comunciar la ventana de autenticación con la ventana principal
            en el que se guardará los valores necesarios para saber si es un usuario autenticado y si es un administrador.
        @author lemartinezm@unah.hn
        @version 1.0.0
    """
    def buildWindow(self, user):
        self.master.geometry('500x170')
        self.master.resizable(width=0, height=0)
        self.master.title("Auth Window")
        self.master.transient(master=self.parent)
        self.master.focus_set()
        
        """
            Funcion encargada de verificar si los datos introducidos son correctos y si estos pertenecen a un usuario registrado.
            @author lemartinez,@unah.hn
            @version 1.0.0
        """
        def isAuth():
            try:
                username = usernameInput.get()
                password = passwordInput.get()

                if( username == "" or password == ""):
                    messagebox.showwarning("Warning", "Fill in all fields.", parent=self)
                elif not(re.match(r"\w+",username) or re.match(r"[A-Za-z0_9]+", password)):
                    messagebox.showerror("Error","You have used illegal characters", parent=self)
                else:
                    user["isAuth"], user["isAdmin"] = am.isAuth(username, password)

                if not user['isAuth']:
                    messagebox.showerror("Error","Incorrect password", parent=self)
                else:
                    self.master.destroy()


            except Exception:
                pass

        usernameLabel = tk.Label(self.master, text='Username')
        usernameInput = tk.Entry(self.master)
        passwordLabel = tk.Label(self.master, text='Password')
        passwordInput = tk.Entry(self.master, show="*")
        doneButton = tk.Button(self.master, text="Done", command=isAuth)
        usernameLabel.pack()
        usernameInput.focus()
        usernameInput.pack()
        passwordLabel.pack()
        passwordInput.pack()
        doneButton.pack();