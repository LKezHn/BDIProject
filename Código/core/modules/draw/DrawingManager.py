# -*- coding: utf-8 -*-

from ..database.MySQLEngine import MySQLEngine

engine = MySQLEngine()

"""
Clase encargada del manejo de los dibujos llamando al motor mysql
@authors lemartinezm@unah.hn eglopezl@unah.hn
@version 1.0.0
"""
class DrawingManager:
    def __init__(self):
        pass

    #Metodo que obtiene los dibujos
    def getDraws(self, id_user, user_role):
        if user_role == 1:
            res = engine.call('sp_getDrawingList', 'select')
            if res:
                for value in res:
                    return value.fetchall()
        else:
            res = engine.call('sp_getUserDrawingList', values = [id_user])
            if res:
                for value in res:
                    return value.fetchall()
        return False