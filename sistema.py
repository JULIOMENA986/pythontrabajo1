from Alumnos.Alumnos import Alumnos
from Grupos.Grupo import Grupos
from Materias import Materias
class sistema:
    def __init__(self):
        self.Alumnos = Alumnos()
        self.Grupos = Grupos()
        self.Materias = Materias()

    def menuPrincipal(self):
            opcionCorrecta = False
            while (not opcionCorrecta):
                print("==================== MENÚ PRINCIPAL ====================")
                print("1.- Mostrar")
                print("2.- Insertar")
                print("3.- Eliminar")
                print("4.- Mostrar todo")
                print("5.- Mostrar uno")
                print("6.- Salir")
                print("========================================================")
            opcion = int(input("Seleccione una opción: "))



