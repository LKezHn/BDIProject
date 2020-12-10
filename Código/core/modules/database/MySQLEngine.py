# -*- coding: utf-8 -*-

import mysql.connector, os
from configparser import ConfigParser

""" Clase de que se conecta con la Base de datos y es el motor mysql
@authors lemartinezm@unah.hn eglopezl@unah.hn
@version 1.0.0
"""
class MySQLEngine:
    
    def __init__(self, database = 1):
        self.getConfig(database)
        
    #Metodo donde esta la configuracion de la conexion a la Base de Datos
    def getConfig(self, database):
        config = ConfigParser()
        config.read('%s/config.ini' % os.path.dirname(os.path.abspath(__file__)))
        if database == 1:
            self.server = config['DATABASE']['server']
            self.port = config['DATABASE']['port']
            self.user = config['DATABASE']['user']
            self.password = config['DATABASE']['password']
            self.database = config['DATABASE']['database']
        elif database == 2:
            self.server = config['BACKUP']['server']
            self.port = config['BACKUP']['port']
            self.user = config['BACKUP']['user']
            self.password = config['BACKUP']['password']
            self.database = config['BACKUP']['database']

    def start(self):
        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )

        #Enlace
        self.link = self.con.cursor()

    def select(self, query):
        self.link.execute(query)
        return self.link.fetchall()
    
    def selectOne(self, query):
        self.link.execute(query)
        return self.link.fetchone()

    """
        Método encargado de insersión de datos en la Base de Datos
        @param query Es la query a ejecutar
        @author lemartinezm@unah.hn
        @version 1.0.0
    """
    def insert(self, query):
        self.link.execute(query)
        self.con.commit()

    """
        Método encargado de eliminacion de datos en la Base de Datos
        @param query Es la query a ejecutar
        @author eglopezl@unah.hn
        @version 1.0.0
    """
    def delete(self,query):
        self.link.execute(query)
        self.con.commit()    

    """
        Método encargado de llamar a un procedimiento almacenado
        @param query Es la query a ejecutar
        @version 1.0.0
    """
    def call(self, nameprocedure, action = 'select' ,values = []):
        if action == 'select':        
            self.start()
            self.link.callproc(nameprocedure,values)
            results = self.link.stored_results()
            self.link.close()
            self.con.close()
            return results
        else:
            try:
                self.start()
                self.link.callproc(nameprocedure,values)
                self.con.commit()
                self.link.close()
                self.con.close()
                return True
            except Exception:
                return False