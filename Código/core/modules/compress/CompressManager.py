# -*- coding: utf-8 -*-
import gzip
from base64 import b64encode, b64decode

class CompressManager:
    def __init__(self):
        pass

    def compress(self, content):
        return b64encode(gzip.compress(content.encode('utf-8'))).decode('utf-8')

    def decompress(self, content):
        return gzip.decompress(b64decode(content)).decode('utf-8')
