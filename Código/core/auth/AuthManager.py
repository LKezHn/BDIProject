# -*- coding: utf-8 -*-

from ..encrypt.EncryptManager import EncryptManager
from ..database.MySQLEngine import MySQLEngine


em = EncryptManager()
engine = MySQLEngine()

"""
    Clase encargada de manejar las acciones relacionadas con la autenticación de un usuario.
    @author lemartinezm@unah.hn
    @version 1.0.0
    @date 2020/12/01
"""
class AuthManager:
    def __init__(self):
        pass

    """
        Método encargado de autenticar si un usuario esta registrado, si es administrador u operador, asi mismo si los datos
        ingresados no son correctos.
        @param username Es el nombre de usuario a autenticar ingresado por el usuario.
        @param password Es la contraseña a autenticar ingresada por el usuario.
        @return True, True Si el usuario esta registrado en la Base de Datos y posee el rol de Administrador.
        @return True, False Si el usuario esta registrado rn la Base de Daots y posee el rol de Operador.
        @return False, False Si no se encontró el usuario ingresado.
        @author lemartinezm@unah.hn
        @version 1.0.0
    """
    def isAuth(self, username, password):
        response = engine.call('sp_authUser', [username])
        for value in response:
            encryptedPassword = list(value.fetchone())[0]
        
        if (username == 'admin' and password == encryptedPassword):
            return True, True
        elif username != 'admin':
            if(encryptedPassword and password == encryptedPassword):
                return True, False
            elif(encryptedPassword and password != encryptedPassword):
                return False, False
        else:
            return False, False

    """
        Método encargado de cambiar los colores de lápiz y de relleno del programa.
        @param pen_color Es el valor que se desea establecer como color de lápiz.
        @param fill_color El el color que se desea establecer como color de relleno.
        @author lemartinezm@unah.hn
        @version 1.0.0
    """
    def changeColors(self, pen_color, fill_color):
        response = engine.callUpdateProcedure('sp_updateColorConfig', [pen_color, fill_color])
        
    """
        Método encargado de obtener el color de lapiz que debe ser usado por el programa.
        @return penColor Es un string que contiene el valor del color de lapiz en formato hexadecimal.
        @author lemartinezm@unah.hn
        @version 1.0.0
    """
    def getPenColor(self):
        response = engine.call('sp_getColorConfig')
        for value in response:
            penColor = list(value.fetchone())[0]
        return penColor

    """
        Método encargado de obtener el color de relleno que debe ser usado por el programa.
        @return fillColor Es un string que contiene el valor del color de relleno en formato hexadecimal.
        @author lemartinezm@unah.hn
        @version 1.0.0
    """
    def getFillColor(self):
        response = engine.call('sp_getColorConfig')
        for value in response:
            fillColor = list(value.fetchone())[1]
        return fillColor