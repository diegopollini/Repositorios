# Creación de una clase simple llamada Vehículo
class Vehiculo:
	# Este tipo de atributo se denomina atributo de clase, véase que se encuentra
	# definido fuera del __init__, y por lo tanto será genérico a nivel de la clase, y no propio de cada instancia
	ctdVehiculosFlota = 0

	# Recordar que el método __init__ es el constructor, se ejecuta de forma automática
	# cada vez que se instancia un objeto de la clase
	# La palabra reservada self hacer referencia a cada instancia (cada objeto) que se cree.
	# Además de self, el constructor puede recibir otros argumentos que se desee pasar (patente e iid en este caso)
	def __init__(self, patente, iid):
		self.iid = iid
		self.patente = patente
		Vehiculo.agregarVehiculo()

	# El decorador (@classmethod) permite definir un método que solo podrá modificar atributos de clase
	# pero no tendrá acceso a modificar atributos internos de cada instancia
	@classmethod
	def agregarVehiculo(clase):
		clase.ctdVehiculosFlota += 1

def main():
	# Creamos 2 vehículos (2 instancias de la clase Vehiculo), pasando los argumentos
	# que el constructor (método __init__) especifica.
	v1 = Vehiculo("ABC333AA", 15)
	v2 = Vehiculo("ABC333AB", 17)

	# Accedemos de forma directa al valor del atributo de clase ctdVehiculosFlota.
	# Si bien esto es válido, existen mejores prácticas para lograr mayor integridad a nivel del código.
	# Por lo general lo aconsejable es activar un método que retorne el valor actual de un atributo.
	print(Vehiculo.ctdVehiculosFlota)
	print(v1.patente)
	print(v2.patente)


if (__name__ == "__main__"):
	main()