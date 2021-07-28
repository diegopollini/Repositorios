# Librerías
import time


# Main
LUCES = [
	{ "nombre": "________VDE________", "color": "\x1b[0;30;42m", "demora": 5 },
	{ "nombre": "________AMA________", "color": "\x1b[3;30;43m", "demora": 2 },
	{ "nombre": "________RJO________", "color": "\x1b[0;30;41m", "demora": 5 }
]
	
luzActiva = 0
while(True):
	print(LUCES[luzActiva]["color"] + LUCES[luzActiva]["nombre"] + "\x1b[0m")
	time.sleep(LUCES[luzActiva]["demora"])

	luzActiva += 1
	if (luzActiva == len(LUCES)):
		luzActiva = 0