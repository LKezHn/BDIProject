import tkinter as tk, re
from tkinter import scrolledtext as st, messagebox
from tkinter import ttk

from ..modules.admin.AdminActionsManager import AdminActionsManager

aam = AdminActionsManager()
class AdminWindow(tk.Frame):

    def __init__(self,master,parent):
        super().__init__(master)
        self.parent = parent
        self.master = master
        self.buildWindow()
        
    def isValidField(self, field, typeOfField):
        if field != "":
            if typeOfField == 'password':
                if not re.match(r"[A-Za-z0-9]+", field):
                    return False
            elif typeOfField == 'text':
                if not re.match(r"\w+",field):
                    return False
        else:
            return False

        return True

    def addNewUser(self):
        if(self.isValidField(self.usernameValue.get(), "text") and self.isValidField(self.passwordValue.get(), "password")):
            res = aam.addUser(self.usernameValue.get(), self.passwordValue.get())
            if res:
                messagebox.showinfo("Done!", "User added")
                self.usernameValue.set("")
                self.passwordValue.set("")
        else:
            messagebox.showerror("Error","You have used illegal characters and fill all the fields", parent=self)

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
        self.labelName.grid(column=0, row=0, padx=85, pady=100)
        self.usernameLabel = ttk.Label(self.labelName, text="Username:")
        self.usernameLabel.grid(column=0, row=0, padx=10, pady=10)
        self.usernameValue = tk.StringVar()
        self.username = ttk.Entry(self.labelName, textvariable=self.usernameValue)
        self.username.grid(column=1, row=0, padx=10, pady=10)
        self.passwordLabel = ttk.Label(self.labelName, text="Password:")
        self.passwordLabel.grid(column=0, row=1, padx=10, pady=10)
        self.passwordValue = tk.StringVar()
        self.password = ttk.Entry(self.labelName, textvariable=self.passwordValue)
        self.password.grid(column=1, row=1, padx=10, pady=10)
        self.addBtn = ttk.Button(self.labelName, text="Confirmar", command=self.addNewUser) #Forma completa => self.addBtn = ttk.Button(self.labelName, text="Confirmar", command=AccionAEjecutar)
        self.addBtn.grid(column=1, row=2, padx=10, pady=10)


        
        self.updateUser = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.updateUser, text="Modificar Usuario")
        self.labelUpdateName = ttk.LabelFrame(self.updateUser, text="Usuario")
        self.labelUpdateName.grid(column=0, row=0, padx=85, pady=110)
        self.userToUpdateLabel = ttk.Label(self.labelUpdateName, text="Username:")
        self.userToUpdateLabel.grid(column=0, row=0, padx=10, pady=10)
        self.userToUpdateValue = tk.StringVar()
        self.userToUpdate = ttk.Entry(self.labelUpdateName, textvariable=self.userToUpdateValue)
        self.userToUpdate.grid(column=1, row=0, padx=10, pady=10)
        self.newUsernameLabel = ttk.Label(self.labelUpdateName, text="New Username:")
        self.newUsernameLabel.grid(column=0, row=1, padx=10, pady=10)
        self.newUsernameValue = tk.StringVar()
        self.newUsername =  ttk.Entry(self.labelUpdateName, textvariable=self.newUsernameValue)
        self.newUsername.grid(column=1, row=1, padx=10, pady=10)
        self.newPasswordLabel = ttk.Label(self.labelUpdateName, text="New Password:")
        self.newPasswordLabel.grid(column=0, row=2, padx=10, pady=10)
        self.newPasswordValue = tk.StringVar()
        self.newPassword = ttk.Entry(self.labelUpdateName, textvariable=self.newPasswordValue)
        self.newPassword.grid(column=1, row=2, padx=10, pady=10)
        self.updateBtn = ttk.Button(self.labelUpdateName, text="Confirmar") #Lo mismo que el anterior
        self.updateBtn.grid(column=1, row=5, padx=10, pady=10)

        self.deleteUser = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.deleteUser, text="Eliminar Usuario")
        self.labelDeleteName = ttk.LabelFrame(self.deleteUser, text="Usuario")
        self.labelDeleteName.grid(column=0, row=0, padx=85, pady=100)
        self.userToDeleteLabel = ttk.Label(self.labelDeleteName, text="User to Delete:")
        self.userToDeleteLabel.grid(column=0, row=0, padx=10, pady=10)
        self.deleteUserValue = tk.StringVar()
        self.userToDelete = ttk.Entry(self.labelDeleteName, textvariable=self.deleteUserValue)
        self.userToDelete.grid(column=1, row=0, padx=10, pady=10)
        self.deleteBtn = ttk.Button(self.labelDeleteName, text="Confirmar")
        self.deleteBtn.grid(column=1, row=2, padx=10, pady=10) 


        self.usersList = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.usersList, text="Listar Usuarios")
        self.labelList = ttk.LabelFrame(self.usersList, text="Usuario")
        self.labelList.grid(column=0, row=0, padx=5, pady=10)
        self.listBtn = ttk.Button(self.labelList, text="Listado completo")
        self.listBtn.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelList, width=45, height=22)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

        

        self.choiseBar.grid(column=0, row=0)

        
        
        

    
