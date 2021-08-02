# Librerías


# Definiciones
# Clase muy sencilla, con un atributo de clase (patas), el constructor (__init__) que recibe 2 argumentos,
# (nombre y raza), y un solo método (ladrar)
class Perro():
	patas = 4
	
	def __init__(self, nombre, raza):
		self.nombre = nombre
		self.raza = raza

	def ladrar(self):
		print(f"{self.nombre} ladra")


# Main
def main():
	# Creamos 2 instancias de la clase Perro (2 perros), y hacemos que ladren
	perro1 = Perro("Batuque", "Galgo")
	perro2 = Perro("Pochoclo", "San Bernardo")
	perro1.ladrar()
	perro2.ladrar()

	# try:
	# 	perro1.ladrar()
	# except Exception as e:
	# 	print(e)

if (__name__ == '__main__'):
	main()