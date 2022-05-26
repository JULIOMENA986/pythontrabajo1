from Materia import Materia
import re
import os 
class InterfaceMateria():
    def __init__(self):
        self.lista = Materia()
    
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
    def nuevaMateria(self):
        p = Materia()
        p.nombre = input("Nombre  materia: ")
        p.calificacion = float(input("Calificacion: "))
        return p
    def mostrarMateria(self, lista= None):
        self.cls()
        print("\n\n" + "-" * 10 + "Datos de materia" + "-" * 10)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(20) + "\t\t" + "Calificacion".ljust(20))
        i =0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p.nombre).ljust(20) + "\t\t" + str(p.calificacion))
            i += 1
        input("oprime enter para continuar .....")
    
    def buscarMateria(self, code):
        mylista = [p for p in self.lista if p.nombre == code]
        self.mostrarMateria(mylista)

    def getListaMateria(self):
        return self.lista

    def modificarMateria(self):
        id = input("Ingrese el id de la materia a modificar: ")
        id = int(id)
        p = self.lista.getLista()[id]
        cadena = input("Ingrese el nuevo nombre de la materia: ")
        if(len(cadena)>0):
            p.nombre = cadena
        else:
            print("No se modifico el nombre")
        if(len(cadena)>0):
            p.calificacion = float(input("Ingrese la nueva calificacion: "))
        else:
            print("No se modifico la calificacion")
        self.lista.update(id, p)

    def eliminarMateria(self):
        id = input("Ingrese el id de la materia a eliminar: ")
        id = int(id)
        print (self.lista.getMateria(id))
        self.lista.delete(self.lista.getMateria(id))
    
    def menuMaterias(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 10 + "Menú materias" + "-" * 10)
            print("1. Agregar materia")
            print("2. Modificar materia")
            print("3. Eliminar materia")
            print("4. Buscar materia")
            print("5. Mostrar materias")
            print("0. Salir")
            a = int(input("Ingrese una opcion: "))
            if a == 1:
                p = self.nuevaMateria()
                self.lista.add(p)
            elif a == 2:
                self.mostrarMateria()
                self.modificarMateria()
            elif a == 3:
                self.mostrarMateria()
                self.eliminarMateria()
            elif a == 4:
                code = input("Ingrese el codigo de la materia: ")
                self.buscarMateria(code)
            elif a == 5:
                self.mostrarMateria()
            elif a == 0:
                break
            else:
                print("Opcion no valida")
                input("oprime enter para continuar .....")


if (__name__ == "__main__"):
    p = InterfaceMateria()
    p.menuMaterias()
