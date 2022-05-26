from Grupo import Grupos
import re
import os 

class InterfaasGrupos():
    def __init__(self):
        self.lista = Grupos()
    
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
    def nuevoGrupo(self):
        p = Grupos()
        p.especialidad = input("especialidad: ")
        p.grupo = input("Grupo asignado: ")
        p.seccion = input("Seccion asignada: ")
        p.edificio = input("Edificio asignada: ")
        return p
    def mostrarGrupo(self, lista= None):
        self.cls()
        print("\n\n" + "-" * 10 + "Datos del Grupo" + "-" * 10)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'especialidad'.ljust(20) + "\t\t" + "Grupo asignado".ljust(20) + "\t\t" + "Seccion asignada".ljust(20) + "\t\t" + "Edificio asigado".ljust(20))
        i =0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p.especialidad).ljust(20) + "\t\t" + str(p.grupo) + "\t\t" + str(p.seccion) + "\t\t" + str(p.edificio))
            i += 1
        input("oprime enter para continuar .....")
    
    def buscarGrupo(self, code):
        mylista = [p for p in self.lista if p.Grupo == code]
        self.mostrarGrupo(mylista)

    def getListagrupo(self):
        return self.lista

    def modificarGrupo(self):
        id = input("Ingrese el id de la materia a modificar: ")
        id = int(id)
        p = self.lista.getLista()[id]
        cadena = input("Ingrese el nuevo nombre de la materia: ")
        if(len(cadena)>0):
            p.Grupo = cadena
        else:
            print("No se modifico el Grupo")
        if(len(cadena)>0):
            p.calificacion = float(input("Ingrese el Nuevo Grupo: "))
        else:
            print("No se modifico El Grupo")
        self.lista.update(id, p)

    def eliminarGrupo(self):
        id = input("Ingrese el id del Grupo a eliminar: ")
        id = int(id)
        print (self.lista.getGrupo(id))
        self.lista.delete(self.lista.getGrupo(id))
    
    def menuGrupo(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 10 + "Menú Grupo" + "-" * 10)
            print("1. Agregar Grupo")
            print("2. Modificar Grupo")
            print("3. Eliminar Grupo")
            print("4. Buscar Grupo")
            print("5. Mostrar Grupo")
            print("0. Salir")
            a = int(input("Ingrese una opcion: "))
            if a == 1:
                p = self.nuevoGrupo()
                self.lista.add(p)
            elif a == 2:
                self.mostrarGrupo()
                self.modificarGrupo()
            elif a == 3:
                self.mostrarGrupo()
                self.eliminarGrupo()
            elif a == 4:
                code = input("Ingrese el codigo del Grupo: ")
                self.buscarGrupo(code)
            elif a == 5:
                self.mostrarGrupo()
            elif a == 0:
                break
            else:
                print("Opcion no valida")
                input("oprime enter para continuar .....")


if (__name__ == "__main__"):
    p = InterfaasGrupos()
    p.menuGrupo()
