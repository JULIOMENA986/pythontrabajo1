from Alumnos import Alumnos
import re
import os 

class interfasalumno:
 def __init__(self):
        self.Alumnos = Alumnos()
def cls(self):
    os.system('cls' if os.name=='nt' else 'clear')

def nuevoalumno(self):
    p = Alumnos()
    p.nombre = input("Nombre Alumno:")
    p.telefono = input("Telefono Alumno:")
    p.direccion = float(input("Dirección Alumno:"))
    return p

def mostraralumno(self,lista=None):
	self.cls()
	print("\n\n"+"*"*30+"Datos Alumno"+"*"*30)
	if(lista == None):
		lista2 = self.lista
	else:
		lista2 = lista
		print("ID".ljust(5)+"\t\t"+"Nombre")
		i=0	
		for p in lista2:
			print(str(i).ljust(5)+"\t\t"+str(p))
		input('enter padrino')
def buscarMateria(self, code):
        mylista = [p for p in self.lista if p.nombre == code]
        self.mostrarMateria(mylista)

def eliminaralumno(self):
	id = input("Eliminar por el ID")
	id= int(id)
	print(self.lista.mostrar(id))
	self.lista.eliminar(self.lista.mostrar(id))

def menualumnos(self):
	a = 10
	while a!=0:
		self.cls()
		print("\n\n"+"*"*30+"Sistema"+"*"*30)
		print("1) Modificar")
		print("2) Insertar")
		print("3) Eliminar ")
		print("4) Mostrar todo")
		print("5) Mostrar uno")
		print("0) Salir")
		a=input("Selecciona una opción: ")
		if (a == '1'):
			p = self.nuevoalumno()
			self.lista.add(p)
		elif (a == '2'):
			self.mostraralumno()
			self.modificaralumno()
		elif (a == '3'):
			self.mostraralumno()
			self.eliminaralumno()
		elif (a == '4'):
			self.mostraralumno()
		elif (a == '0'):
			break
		else:
			print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
			input()
	
if __name__=='__main__':
	ip=interfasalumno()
	ip.menualumnos()