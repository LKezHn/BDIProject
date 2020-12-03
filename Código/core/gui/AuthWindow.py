# -*- coding: utf-8 -*-

import tkinter as tk, re
from tkinter import messagebox
from ..auth.AuthManager import AuthManager

am = AuthManager()

class AuthWindow(tk.Frame):
    def __init__(self, master, parent, user = {}):
        super().__init__(master)
        self.parent = parent
        self.master = master
        self.buildWindow(user)

    def buildWindow(self, user):
        self.master.geometry('500x170')
        self.master.resizable(width=0, height=0)
        self.master.title("Auth Window")
        

        def isAuth():
            try:
                username = usernameInput.get()
                password = passwordInput.get()

                if( username == "" or password == ""):
                    messagebox.showwarning("Warning", "Fill in all fields.", parent=self)
                elif not(re.match(r"\w+",username) or re.match(r"[A-Za-z0_9]+", password)):
                    messagebox.showerror("Error","You have used illegal characters", parent=self)
                else:
                    pass
                
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
        usernameInput.pack()
        passwordLabel.pack()
        passwordInput.pack()
        doneButton.pack();