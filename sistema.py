import os
from Alumnos.interfasalumnos import interfasalumno
from Grupos.InterfaasGrupos import InterfaasGrupos
from Materias.InterfaceMateria import InterfaceMateria


class sistema:
    def __init__(self):
        self.interfasalumno = interfasalumno()
        self.InterfaasGrupos = InterfaasGrupos()
        self.InterfaceMateria = InterfaceMateria()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menuPrincipal(self):
        a = 10;
        while a != 0:
            self.cls()
            print("\n\n" + "*" * 40 + "Menu de Principal" + "*" * 40)
            print("M) Materias")
            print("A) Alumnos")
            print("G) Grupos")
            print("0) Salir")
            a = input("Selecciona una opción: ")
            if a.upper() == 'M':
                p = self.InterfaceMateria.menuMaterias()
            elif a.upper() == 'A':
                p = self.interfasalumno.menuAlumnos()
            elif a.upper() == 'G':
                p = self.InterfaasGrupos.menuGrupo()
            elif a == '0':
                break;
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()


if __name__ == '__main__':
    ip = sistema()
    ip.menuPrincipal()
