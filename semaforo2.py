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
		self.__luzActiva = 0
		self.__modo = "DIURNO"
		self.__tiempoAnterior = 0
		self.__luzEncendida = False
		self.__tiempoAnterior = time.perf_counter()
		Semaforo.LUCES[0]["demora"] = tiempoVde
		Semaforo.LUCES[1]["demora"] = tiempoAma
		Semaforo.LUCES[2]["demora"] = tiempoRjo
		Semaforo.LUCES[3]["demora"] = tiempoApa
	
	def __encender(self, luz):
		if not (self.__luzEncendida):
			print(Semaforo.LUCES[luz]["color"] + Semaforo.LUCES[luz]["nombre"] + "\x1b[0m")
			self.__luzEncendida = True

	def ciclar(self):
		if (self.__modo == "DIURNO"):
			if not (self.__luzEncendida):
				self.__encender(self.__luzActiva)
			elif (time.perf_counter() - self.__tiempoAnterior >= Semaforo.LUCES[self.__luzActiva]["demora"]):
				self.__luzActiva += 1
				self.__luzEncendida = False
				if (self.__luzActiva == len(Semaforo.LUCES) - 1):
					self.__luzActiva = 0
				self.__tiempoAnterior = time.perf_counter()
		else:
			if not (self.__luzEncendida):
				self.__luzActiva = -1 if (self.__luzActiva == 1) else 1
				self.__encender(self.__luzActiva)
			elif (time.perf_counter() - self.__tiempoAnterior >= Semaforo.LUCES[self.__luzActiva]["demora"]):
				self.__luzEncendida = False
				self.__tiempoAnterior = time.perf_counter()
	
	def setearModo(self, modo):
		self.__luzActiva = 0 if (modo == "DIURNO") else 1
		self.__modo = modo

	def verModo(self):
		return self.__modo