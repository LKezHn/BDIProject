# -*- coding: utf-8 -*-

from ..database.MySQLEngine import MySQLEngine

engine = MySQLEngine()
backupEngine = MySQLEngine(2)

"""
Clase encargada de conectarse con el motor mysql
@authors eglopezl@unah.hn lemartinezm@unah.hn
@version 1.0.0
"""
class AdminActionsManager:
    def __init__(self):
        pass

    """
    Metodo que hace el llamado agregar usuario al motro mysql
    @param username Nombre del usuario nuevo
    @param password Contraseña del usuario
    @author lemartinezm@unah.hn
    @version 1.0.0
    """
    def addUser(self, username, password):
        res = engine.call('sp_addUser', 'insert', [username, password, 2])        
        backupEngine.call('sp_addUser', 'insert', [username, password, 2])        
        if res:
            return True
        return False

    """
    Metodo encargado de hacer el llamado al motor mysql con el procedure de obtener usuarios
    @author eglopezl@unah.hn
    @version 1.0.0
    """
    def getUsers(self):
        res = engine.call('sp_getAllUsers', 'select')
        if res:
            engine.call('sp_visualizeUserList', 'insert', [1])
            for value in res:
                return value.fetchall()
        return False

    """
    Metodo encargado de borrar usuario mediante el llamada al motor mysql.
    @param username Nombre del usuario que se desea eliminar
    @author eglopezl@unah.hn
    @version 1.0.0
    """ 
    def deleteUser(self, username):
        res = engine.call('sp_deleteUser', 'delete', [username])
        if res:
            return True 
        return False 

    """
    Metodo que modifica un usuario.
    @param username Nombre del usuario que se desea modificar.
    @param newUsername Nuevo nombre que queremos
    @param newPassword Contraseña nueva del usuario
    @author eglopezl@unah.hn
    @version 1.0.0
    """
    def updateUser(self, username, newUsername, newPassword):
        res = engine.call('sp_updateUserInfo', 'update', [username, newUsername, newPassword])
        backupEngine.call('sp_updateUserInfo', 'update', [username, newUsername, newPassword])
        if res:
            return True
        return False