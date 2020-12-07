# -*- coding: utf-8 -*-

from ..database.MySQLEngine import MySQLEngine
from ..encrypt.EncryptManager import EncryptManager

engine = MySQLEngine()
em = EncryptManager()

class AdminActionsManager:
    def __init__(self):
        pass

    def addUser(self, username, password):
        encryptedPassword = em.encrypt(password)
        print(encryptedPassword)
        res = engine.call('sp_addUser', 'insert', [username, encryptedPassword, 2])        
        if res:
            return True
        return False

    def getUsers(self):
        res = engine.call('sp_getAllUsers', 'select')
        if res:
            for value in res:
                return value.fetchall()
        return False        