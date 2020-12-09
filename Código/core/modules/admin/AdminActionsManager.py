# -*- coding: utf-8 -*-

from ..database.MySQLEngine import MySQLEngine

engine = MySQLEngine()
backupEngine = MySQLEngine(2)

class AdminActionsManager:
    def __init__(self):
        pass

    def addUser(self, username, password):
        res = engine.call('sp_addUser', 'insert', [username, password, 2])        
        backupEngine.call('sp_addUser', 'insert', [username, password, 2])        
        if res:
            return True
        return False

    def getUsers(self):
        res = engine.call('sp_getAllUsers', 'select')
        if res:
            engine.call('sp_visualizeUserList', 'insert', [1])
            for value in res:
                return value.fetchall()
        return False

    def deleteUser(self, username):
        res = engine.call('sp_deleteUser', 'delete', [username])
        if res:
            return True 
        return False 

    def updateUser(self, username, newUsername, newPassword):
        res = engine.call('sp_updateUserInfo', 'update', [username, newUsername, newPassword])
        backupEngine.call('sp_updateUserInfo', 'update', [username, newUsername, newPassword])
        if res:
            return True
        return False