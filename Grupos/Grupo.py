from Alumnos.Alumnos import Alumnos
from Materias.Materia import Materia
import copy
class Grupo(Alumnos):
    def __init__(self, idgrupos=0, especialidad="", grupo ="", seccion="", edificio="",lista=list()):
        self.idgrupos = idgrupos
        self.especialidad = especialidad
        self.grupo = grupo
        self.seccion = seccion
        self.edificio = edificio
        self.lista = lista
        self.__idx__ = 0  
        super(Grupo, self).__init__('../JSONS/Grupos.json')
        self.nombrefile = "../JSONS/Grupos.json"
        self.filename = self.nombrefile  

    def add(self, Grupos):
        self.lista.append(Grupos)
    
    def remove(self, Grupos):
        self.lista.remove(Grupos)

    def getGrupo(self, index):
        return self.lista[index]

    def update(self, index,Grupos):
        self.lista[index] = Grupos
    
    def getLista(self):
        return self.lista

    def __str__(self):
        return self.nombre + " " + str(self.especialidad)+ " " + str(self.grupo)+ " " + str(self.seccion)+ " " + str(self.edificio)

    def getDirectory(self):
        return{
            "nombre": self.nombre,
            "especialidad": self.especialidad,
            "grupo": self.grupo,
            "seccion": self.seccion,
            "edificio": self.edificio
        }

    def __iter__(self):
        self.__idx__ = 0
        return self

    def __next__(self):
        if self.__idx__ < len(self.lista):
            x = self.lista[self.__idx__]
            self.__idx__ += 1
            return x
        else:
            raise StopIteration

    def __str__(self):
        return self.nombre.ljust(20) + ' \t\t' + self.especialidad.ljust(20)+ ' \t\t' + self.grupo.ljust(20)+ ' \t\t' + self.seccion.ljust(20)+ ' \t\t' + self.edificio(20)

    def toObjects(self):
        lista = list()
        return  lista
        data = self.getDataJson()
        if(data):
           for x in data:
              lista.append(Materia(nombre=x['nombre'], especialidad=x["especialidad"], grupo=x["grupo"], seccion=x["seccion"], edificio=x["edificio"]))
        self.lista = lista

    def getDictory(self):
        return {
             "nombre": self.nombre,
            "especialidad": self.especialidad,
            "grupo": self.grupo,
            "seccion": self.seccion,
            "edificio": self.edificio
        }

    def listDict(self):
        listDiccionario = list()
        for x in self.lista:
            listDiccionario.append(x.__dict__)
            print(x.getDictory())
        return listDiccionario;

    def __iter__(self):
        self.__idx__ = 0
        return self

    def __next__(self):
        if self.__idx__ < len(self.lista):
            x = self.lista[self.__idx__]
            self.__idx__ += 1
            return x
        else:
            raise StopIteration



    
