# -*- coding: utf-8 -*-

from .AES import AESCipher

# En lugar de "admin" se pasaria la contraseña del usuario administrador desde la base de datos
aem = AESCipher("admin")

class EncryptManager:
    def __init__(self):
        pass

    def encrypt(self, text):
        #print("Encrypted: %s" % aem.encrypt(text))
        return aem.encrypt(text)

    def decrypt(self, text):
        return aem.decrypt(text)


