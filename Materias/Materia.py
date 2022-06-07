from Jsonconexion import JsonFile
import copy

class Materia(JsonFile):
    def __init__(self, nombre="", calificacion=0.0, lista=list()):
        self.nombre = nombre
        self.calificacion = calificacion
        self.lista = lista
        self.__idx__ = 0
        super(Materia, self).__init__('../JSONS/Materia.json')
        self.nombrefile = "../JSONS/Materia.json"
        self.filename = self.nombrefile

    def add(self, Materia):
        self.lista.append(Materia)

    def delete(self, Materia):
        self.lista.remove(Materia)

    def getMateria(self, index):
        return self.lista[index]

    def update(self, index,Materia):
        self.lista[index] = Materia

    def getLista(self):
        return self.lista

    def __str__(self):
        return self.nombre + " " + str(self.calificacion)

    def getDirectory(self):
        return{
            "nombre": self.nombre,
            "calificacion": self.calificacion
        }

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

    def __str__(self):
        return self.nombre.ljust(20) + ' \t\t' + self.calificacion.ljust(20)

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
         lista.append(Materia(nombre=x['nombre'], calificacion=x["calificacion"]))
        self.lista = lista

    def getDictory(self):
        return {
            "nombre": self.nombre,
            "calificacion": self.calificacion
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


#if (__name__=='__main__'):
   # cal = Materia()
    #cal.add(Materia(1, "Matematicas", 10))
    #cal.add(Materia(2, "Lenguaje", 8))
    #cal.add(Materia(3, "Ciencias", 9))
    #cal.add(Materia(4, "Historia", 7))
    #cal.add(Materia(5, "Geografia", 6))
    #cal1=copy.copy(cal)
    #cal.add(cal1)

    #for a in cal.getLista():
     #   print(a)
    #print(cal.toObjects())
    #print(cal.getMateria(1))

