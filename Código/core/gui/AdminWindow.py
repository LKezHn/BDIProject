import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import ttk

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
        self.choiseBar = ttk.Notebook(self.master)
        

        
        self.addUser = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.addUser, text="Crear Usuario")
        self.labelName = ttk.LabelFrame(self.addUser, text="Usuario")
        self.labelName.grid(column=0, row=0, padx=5, pady=10)
        self.usernameLabel = ttk.Label(self.labelName, text="Username:")
        self.usernameLabel.grid(column=0, row=0, padx=4, pady=4)
        self.usernameValue = tk.StringVar()
        self.username = ttk.Entry(self.labelName, textvariable=self.usernameValue)
        self.username.grid(column=1, row=0, padx=4, pady=4)
        self.passwordLabel = ttk.Label(self.labelName, text="Password:")
        self.passwordLabel.grid(column=0, row=1, padx=4, pady=4)
        self.passwordValue = tk.StringVar()
        self.password = ttk.Entry(self.labelName, textvariable=self.passwordValue)
        self.password.grid(column=1, row=1, padx=4, pady=4)
        self.addBtn = ttk.Button(self.labelName, text="Confirmar") #Forma completa => self.addBtn = ttk.Button(self.labelName, text="Confirmar", command=AccionAEjecutar)
        self.addBtn.grid(column=1, row=2, padx=4, pady=4)


        
        self.updateUser = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.updateUser, text="Modificar Usuario")
        self.labelUpdateName = ttk.LabelFrame(self.updateUser, text="Usuario")
        self.labelUpdateName.grid(column=0, row=0, padx=5, pady=10)
        self.userToUpdateLabel = ttk.Label(self.labelUpdateName, text="Username:")
        self.userToUpdateLabel.grid(column=0, row=0, padx=4, pady=4)
        self.userToUpdateValue = tk.StringVar()
        self.userToUpdate = ttk.Entry(self.labelUpdateName, textvariable=self.userToUpdateValue)
        self.userToUpdate.grid(column=1, row=0, padx=4, pady=4)
        self.newUsernameLabel = ttk.Label(self.labelUpdateName, text="New Username:")
        self.newUsernameLabel.grid(column=0, row=1, padx=4, pady=4)
        self.newUsernameValue = tk.StringVar()
        self.newUsername =  ttk.Entry(self.labelUpdateName, textvariable=self.newUsernameValue)
        self.newUsername.grid(column=1, row=1, padx=4, pady=4)
        self.newPasswordLabel = ttk.Label(self.labelUpdateName, text="New Password:")
        self.newPasswordLabel.grid(column=0, row=2, padx=4, pady=4)
        self.newPasswordValue = tk.StringVar()
        self.newPassword = ttk.Entry(self.labelUpdateName, textvariable=self.newPasswordValue)
        self.newPassword.grid(column=1, row=2, padx=4, pady=4)
        self.updateBtn = ttk.Button(self.labelUpdateName, text="Confirmar") #Lo mismo que el anterior
        self.updateBtn.grid(column=1, row=3, padx=4, pady=4)

        self.deleteUser = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.deleteUser, text="Eliminar Usuario")

        self.usersList = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.usersList, text="Listar Usuarios")
        self.labelList = ttk.LabelFrame(self.usersList, text="Usuario")
        self.labelList.grid(column=0, row=0, padx=5, pady=10)
        self.listBtn = ttk.Button(self.labelList, text="Listado completo")
        self.listBtn.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelList, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

        

        self.choiseBar.grid(column=0, row=0)

        
        
        

    
