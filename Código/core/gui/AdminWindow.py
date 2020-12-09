import tkinter as tk, re
from tkinter import scrolledtext as st, messagebox
from tkinter import ttk
from ..modules.encrypt.EncryptManager import EncryptManager
from ..modules.admin.AdminActionsManager import AdminActionsManager
from ..modules.auth.AuthManager import AuthManager

aam = AdminActionsManager()
em = EncryptManager()
am = AuthManager()

class AdminWindow(tk.Frame):

    def __init__(self,master,parent):
        super().__init__(master)
        self.parent = parent
        self.master = master
        self.buildWindow()

    """
    Metodo encargado de la validacion utlizando expreiones regulares de los campos en los Adminoptions.
    @param valor del de lo ingresado en el input.
    @param tipo de campo del input.
    @author lemartinezm@unah.hn
    """   
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

    """
    Metodo encargado de agregar usuarios, validando los campos correspondientes.
    @author lemartinezm@unah.hn
    """
    def addNewUser(self):
        if(len(self.usernameValue.get()) < 4 or len(self.passwordValue.get()) < 4):
            messagebox.showerror("Error","Username or password too short", parent=self)
        elif(self.isValidField(self.usernameValue.get(), "text") and self.isValidField(self.passwordValue.get(), "password")):
            res = aam.addUser(self.usernameValue.get(), self.passwordValue.get())
            if res:
                messagebox.showinfo("Done!", "User added")
                self.usernameValue.set("")
                self.passwordValue.set("")
                self.getUsersList()
        else:
            messagebox.showerror("Error","You have used illegal characters and fill all the fields", parent=self)

    """
    Metodo que actualiza la lista de usuarios cada vez que se realicen cambios en la base.
    @author lemartinezm@unah.hn
    """
    def getUsersList(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        users = aam.getUsers()
        for user in users:
            if user[2] != "admin":
                self.treeview.insert("", "end", text=user[0], value=(user[1], em.decrypt(user[2]), user[3], user[4]))
            else:
                self.treeview.insert("", "end", text=user[0], value=(user[1], user[2], user[3], user[4]))  

    """
    Metodo de eliminacion de usuarios, Verificando si el usuario existe lo elimina.
    @author eglopezl@unah.hn
    """
    def deleteUserSelected(self):
        if(len(self.deleteUserValue.get()) < 4):
            messagebox.showerror("Error","Username too short", parent=self)    
        elif(self.isValidField(self.deleteUserValue.get(), "text")):
            if self.deleteUserValue.get() == "admin":
                messagebox.showerror("Error", "Admin can't be deleted", parent=self)
            else:
                if am.userIsAuth(self.deleteUserValue.get()):
                    res = aam.deleteUser(self.deleteUserValue.get())
                    if res:
                        messagebox.showinfo("Done!", "User deleted")
                        self.deleteUserValue.set("")
                        self.getUsersList()
                else:
                    messagebox.showerror("Error", "User doesn't exist")            
        else:
            messagebox.showerror("Error","You have used illegal characters and fill all the fields", parent=self)
                  

    """
    Metodo que actualiza el usuario a modificar por su username.
    @author eglopezl@unah.hn
    """
    def updateUserSelected(self):
        if(len(self.userToUpdateValue.get()) < 4 or len(self.newUsernameValue.get()) < 4 or len(self.newPasswordValue.get()) < 4):
            messagebox.showerror("Error","Some field is too short", parent=self)
        elif(self.isValidField(self.userToUpdateValue.get(), "text") and self.isValidField(self.newUsernameValue.get(), "text") and self.isValidField(self.newPasswordValue.get(), "text")):    
            if self.userToUpdateValue.get() == "admin":
                messagebox.showerror("Error","Admin can't be modified")
            else:
                if am.userIsAuth(self.userToUpdateValue.get()):
                    res = aam.updateUser(self.userToUpdateValue.get(), self.newUsernameValue.get(), self.newPasswordValue.get())
                    if res:
                        messagebox.showinfo("Done!", "User update")
                        self.userToUpdateValue.set("")
                        self.newUsernameValue.set("")
                        self.newPasswordValue.set("")
                        self.getUsersList()
                else:
                     messagebox.showerror("Error", "User doesn't exist")           
        else:
            messagebox.showerror("Error","You have used illegal characters and fill all the fields", parent=self)         

                   

    """
    Construccion de la ventana de AdminOPtions.
    @author eglopezl@unah.hn
    """
    def buildWindow(self):
        self.master.title('Admin Window')
        self.master.geometry('500x500')
        self.master.resizable(width=0, height=0)
        self.master.transient(master=self.parent)
        self.master.focus_set()
        self.master.grab_set()
        self.choiseBar = ttk.Notebook(self.master)
        

        """
        Construccion del formulario de crear usuario.
        @author eglopezl@unah.hn
        """
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
        self.addBtn = ttk.Button(self.labelName, text="Confirmar", command=self.addNewUser)
        self.addBtn.grid(column=1, row=2, padx=10, pady=10)


        """
        Se crea formulario para la actualizacion del Usuario especificado por su username.
        @author eglopezl@unah.hn
        """
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
        self.updateBtn = ttk.Button(self.labelUpdateName, text="Confirmar", command=self.updateUserSelected)
        self.updateBtn.grid(column=1, row=5, padx=10, pady=10)


        """Creacion del formulario del Usuario a borrar mediante el username ingresado.
        @author eglopezl@unah.hn
        """
        self.deleteUser = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.deleteUser, text="Eliminar Usuario")
        self.labelDeleteName = ttk.LabelFrame(self.deleteUser, text="Usuario")
        self.labelDeleteName.grid(column=0, row=0, padx=85, pady=100)
        self.userToDeleteLabel = ttk.Label(self.labelDeleteName, text="User to Delete:")
        self.userToDeleteLabel.grid(column=0, row=0, padx=10, pady=10)
        self.deleteUserValue = tk.StringVar()
        self.userToDelete = ttk.Entry(self.labelDeleteName, textvariable=self.deleteUserValue)
        self.userToDelete.grid(column=1, row=0, padx=10, pady=10)
        self.deleteBtn = ttk.Button(self.labelDeleteName, text="Confirmar", command=self.deleteUserSelected)
        self.deleteBtn.grid(column=1, row=2, padx=10, pady=10) 


        """
        Tabla donde se visualizan los usuarios existentes.
        @authors lemartinezm@unah.hn eglopezl@unah.hn
        """
        self.usersList = ttk.Frame(self.choiseBar)
        self.choiseBar.add(self.usersList, text="Listar Usuarios")
        self.treeview = ttk.Treeview(self.usersList, columns=("username", "password", "role", "drawNumber"))
        self.treeview.column("#0", width=40, stretch=False)
        self.treeview.column("username", width=100, stretch=False)
        self.treeview.column("password", width=100, stretch=False)
        self.treeview.column("role", width=100, stretch=False)
        self.treeview.column("drawNumber", width=100, stretch=False)
        self.treeview.heading("#0", text ="id")
        self.treeview.heading("username", text ="Username")
        self.treeview.heading("password", text = "Password")
        self.treeview.heading("role", text = "Role")
        self.treeview.heading("drawNumber", text = "No. Draws")
        users = aam.getUsers()
        for user in users:
            if user[2] != "admin":
                self.treeview.insert("", "end", text=user[0], value=(user[1], em.decrypt(user[2]), user[3], user[4]))
            else:
                self.treeview.insert("", "end", text=user[0], value=(user[1], user[2], user[3], user[4]))     
        
        self.treeview.pack()
        self.choiseBar.grid(column=0, row=0)

        
        

    
