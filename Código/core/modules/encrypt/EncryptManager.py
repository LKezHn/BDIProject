# -*- coding: utf-8 -*-

from .AES import AESCipher

# En lugar de "admin" se pasaria la contraseña del usuario administrador desde la base de datos
aem = AESCipher("admin")

"""
    Clase encargada de manejar la encriptación de los datos que serán ingresados por los usuarios.
    @author lemartinezm@unah.hn
    @version 1.0.0
    @date 2020/12/01 
"""
class EncryptManager:
    def __init__(self):
        pass

    def encrypt(self, text):
        #print("Encrypted: %s" % aem.encrypt(text))
        return aem.encrypt(text)

    def decrypt(self, text):
        return aem.decrypt(text)


