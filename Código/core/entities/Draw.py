# -*- coding: utf-8 -*-

class Draw:
    def __init__(self):
        self.content = {}

    def new(self, info = {}):
        self.id = info['id']
        self.name = info['name']
        self.content = info['content']

    def exists(self):
        if self.content != {}:
            return True
        return False

    def clear(self):
        self.id = 0
        self.name = ""
        self.content = {}
    
    def setDraw(self, content):
        self.content = content