import json

class Database:
    def __init__(self, pathname):
        self.file = open(pathname, 'r+')
    
    def __get_value(self, key):
        self.file.seek(0)
        data = json.load(self.file)
        return data[key]