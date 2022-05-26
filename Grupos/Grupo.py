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
        return self.nombre + " " + str(self.idgrupos)

    def toObjects(self):
        lista = list()
        for x in self.lista:
            lista.append(x.getDirectory())
        return lista

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



    
