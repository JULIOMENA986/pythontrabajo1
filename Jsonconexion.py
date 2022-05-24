import os.path
import json


class JsonFile:
    def __init__(self, filename):
        self.filename = filename

    def getDataJson(self):
        data = []
        if os.path.isfile(self.filename):
            file = open(self.filename, "r")
            data = json.loads(file.read())
        return data
    def toJson(self, listasmaterias): 
         file = open(self.filename, "w")
         file = json.dump([ob.__dict__ for ob in listasmaterias], file, indent=4)    
