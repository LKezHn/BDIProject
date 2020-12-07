# -*- coding: utf-8 -*-

import mysql.connector, os
from configparser import ConfigParser

class MySQLEngine:
    
    def __init__(self):
        self.getConfig()
        

    def getConfig(self):
        config = ConfigParser()
        config.read('%s/config.ini' % os.path.dirname(os.path.abspath(__file__)))
        self.server = config['DATABASE']['server']
        self.port = config['DATABASE']['port']
        self.user = config['DATABASE']['user']
        self.password = config['DATABASE']['password']
        self.database = config['DATABASE']['database']

    def start(self):
        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )

        #print("Version de texto del objeto de conexion a MYSQL: %s" %self.con)

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
        @version 1.0.0
    """
    def insert(self, query):
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