# Definiciones


# Funciones y clases
class Estudiante():
	def __init__(self, nombre, edad, grado):
		self.__nombre = nombre
		self.edad = edad
		self.grado = grado
		# print(f"Estudiante {nombre} creado.")
	
	def mostrarNombre(self):
		return self.__nombre

class Curso():
	semanasDuracion = 16

	def __init__(self, nombre, limiteEstudiantes):
		self.nombre = nombre
		self.limiteEstudiantes = limiteEstudiantes
		self.listaEstudiantes = []
		# print(f"Curso {nombre} creado.")
	
	def agregarEstudiante(self, estudiante):
		if (len(self.listaEstudiantes) < self.limiteEstudiantes):
			self.listaEstudiantes.append(estudiante)
			# print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre}")
			return True
		
		print(f"No se pudo agregar al estudiante {estudiante.nombre}. Max de estudiantes excedido.")
		return False
	
	def mostrarEstudiantes(self):
		print(f"Listado de estudiantes {self.nombre}")
		for item in self.listaEstudiantes:
			print(item.nombre, item.edad, item.grado)
	
	def obtenerGradoPromedio(self):
		sumatoria = 0
		for item in self.listaEstudiantes:
			sumatoria += item.grado
		return int(sumatoria / len(self.listaEstudiantes))

# Main
def main():
	# Creamos Curso
	curso = Curso("Fundamentos de Programación", 2)

	# Creamos estudiantes
	print()
	est1 = Estudiante("Pepe", 20, 90)
	# el atributo nombre es estático (__nombre), por ende solo se puede acceder mediante método
	# Si ejecutáramos print(est1.__nombre), obtendríamos un AttributeError
	print(est1.mostrarNombre())
	
	est2 = Estudiante("José", 22, 90)
	est3 = Estudiante("Augusto", 19, 70)

	print(est2.mostrarNombre())
	print(est3.mostrarNombre())


	# # Agregamos estudiantes a curso
	# print()
	#curso.agregarEstudiante(est1)
	#curso.agregarEstudiante(est2)
	#curso.agregarEstudiante(est3)

	# # Muestro estudiantes del curso
	# print()
	#curso.mostrarEstudiantes()
	#print(f"Promedio grado curso: {curso.obtenerGradoPromedio()}")

if __name__ == '__main__':
	main()