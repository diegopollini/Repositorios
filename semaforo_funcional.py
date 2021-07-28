# Librerías
import time


# Definiciones
def activarLuz(indice, modo):
	LUCES = [
		{ "nombre": "________VDE________", "color": "\x1b[0;30;42m", "demora": 5 },
		{ "nombre": "________AMA________", "color": "\x1b[3;30;43m", "demora": 2 },
		{ "nombre": "________RJO________", "color": "\x1b[0;30;41m", "demora": 5 },
		{ "nombre": "________APA________", "color": "\x1b[0m", "demora": 2 }
	]
	
	if (modo): # Modo Diurno
		print(LUCES[indice]["color"] + LUCES[indice]["nombre"] + "\x1b[0m")
		time.sleep(LUCES[indice]["demora"])
		
		indice += 1
		if (indice == len(LUCES) - 1):
			indice = 0

	else: # Modo Nocturno
		indice = -1 if (indice == 1) else 1
		print(LUCES[indice]["color"] + LUCES[indice]["nombre"] + "\x1b[0m")
		time.sleep(LUCES[indice]["demora"])
	
	return indice


def main():
	modoDiurno = True
	luz = 0 if (modoDiurno) else 1

	while(True):
		luz = activarLuz(luz, modoDiurno)

# Main
if(__name__ == "__main__"):
	main()