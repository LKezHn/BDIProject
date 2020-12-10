# -*- coding: utf-8 -*-
import gzip
from base64 import b64encode, b64decode

"""
Clase que se encarga de comprimir todos los datos que van en la Base de respaldo
@authors lemartinezm@unah.hn eglopezl@unah.hn
@version 1.0.0
"""
class CompressManager:
    def __init__(self):
        pass

    #Metodo que comprime
    def compress(self, content):
        return b64encode(gzip.compress(content.encode('utf-8'))).decode('utf-8')

    #Metodo para descomprimir
    def decompress(self, content):
        return gzip.decompress(b64decode(content)).decode('utf-8')
