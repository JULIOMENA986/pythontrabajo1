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

