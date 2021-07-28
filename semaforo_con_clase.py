# Librerías
from semaforo import Semaforo


# Main
def main():
	semaforo1 = Semaforo(234, 5, 2, 5, 2)
	semaforo1.setearModo("DIURNO")
	
	while(True):
		semaforo1.ciclar()

if __name__ == '__main__':
	main()