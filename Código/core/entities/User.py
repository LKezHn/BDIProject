# -*- coding: utf-8 -*-

from ..modules.auth.AuthManager import AuthManager

class User:
    def __init__(self):
        pass

    def __str__(self):
        return "%d, %s, %d" % (self.id, self.name, self.role)

    def new(self, identifier):
        info = (AuthManager()).getUserInfo(identifier)
        self.id, self.name, self.role = info
        
    def getID(self):
        return self.id
    
    def getRole(self):
        return self.role