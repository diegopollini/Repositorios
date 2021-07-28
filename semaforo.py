# Librerías
import time


# Definiciones
class Semaforo:
	LUCES = [
		{ "nombre": "________VDE________", "color": "\x1b[0;30;42m", "demora": 0 },
		{ "nombre": "________AMA________", "color": "\x1b[3;30;43m", "demora": 0 },
		{ "nombre": "________RJO________", "color": "\x1b[0;30;41m", "demora": 0 },
		{ "nombre": "________APA________", "color": "\x1b[0m", "demora": 0 }
	]

	def __init__(self, id, tiempoVde, tiempoAma, tiempoRjo, tiempoApa):
		self.id = id
		self.__modo = "DIURNO"
		Semaforo.LUCES[0]["demora"] = tiempoVde
		Semaforo.LUCES[1]["demora"] = tiempoAma
		Semaforo.LUCES[2]["demora"] = tiempoRjo
		Semaforo.LUCES[3]["demora"] = tiempoApa
	
	def __encender(self, luz):
		print(Semaforo.LUCES[luz]["color"] + Semaforo.LUCES[luz]["nombre"] + "\x1b[0m")
		time.sleep(Semaforo.LUCES[luz]["demora"])

	def ciclar(self):
		if (self.__modo == "DIURNO"):
			self.__encender(0)
			self.__encender(1)
			self.__encender(2)
		else:
			self.__encender(1)
			self.__encender(-1)
		print()
	
	def setearModo(self, modo):
		self.__modo = modo

	def verModo(self):
		return self.__modo