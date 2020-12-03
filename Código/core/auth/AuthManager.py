# -*- coding: utf-8 -*-

from ..encrypt.EncryptManager import EncryptManager
from ..database.MySQLEngine import MySQLEngine


em = EncryptManager()
engine = MySQLEngine()


class AuthManager:
    def __init__(self):
        pass

    def isAuth(self, username, password):
        response = engine.call('sp_authUser', [username])
        for value in response:
            encryptedPassword = list(value.fetchone())[0]
        
        if (username == 'admin' and password == encryptedPassword):
            return True, True
        elif username != 'admin':
            if(password == encryptedPassword):
                return True, False
        else:
            return False, False

    def changeColors(self, pen_color, fill_color):
        response = engine.callUpdateProcedure('sp_updateColorConfig', [pen_color, fill_color])
        
    def getPenColor(self):
        response = engine.call('sp_getColorConfig')
        for value in response:
            penColor = list(value.fetchone())[0]
        return penColor

    def getFillColor(self):
        response = engine.call('sp_getColorConfig')
        for value in response:
            fillColor = list(value.fetchone())[1]
        return fillColor