from Materias.Materia import Materia

class Alumnos(Materia):
    def __init__(self, idalumnos=0, nombre="", telefono ="", direccion="",lista=list()):
        self.idalumnos = idalumnos
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.lista = lista


    def modificar(self, index, Alumnos):
        self.lista[index] = Alumnos
        
    def insertas(self, Alumnos):
        self.lista.append(Alumnos)

    def eliminar(self, Alumnos):
        self.lista.remove(Alumnos)

    def getmostrartodo(self):
        return self.lista

    def getmostrar(self, index):
        return self.lista[index]

    def getlist(self):
        return self.lista    

    def __str__(self):
        return str(self.idalumnos) + '\t\t' + self.nombre + '\t\t' + self.telefono+ '\t\t' + self.direccion

    def getDirectory(self):
        return{
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion
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
        return self.nombre.ljust(20) + ' \t\t' + self.rfc.ljust(20) + ' \t\t' + self.direccion

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Alumnos(_id=x['_id'], nombre=x['nombre'], rfc=x['rfc'], direccion=x["direccion"]))
        self.lista = lista

    def getDictory(self):
        return {
            "nombre": self.nombre,
            "rfc": self.rfc,
            "direccion": self.direccion
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