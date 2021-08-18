import requests as req


def main():
	#imagen = { "photo": open("semana16/logo_id.png", "rb") }

	URL_TELEGRAM = "https://api.telegram.org/bot"
	TOKEN = "1842138649:AAGlGHONtm2E0cAR1TYavfY2KPmC4fKlNCo"
	ENDPOINT = "sendMessage"
	ID_CHAT = "-538906313"
	TEXTO = "Este es el nuevo texto"
	URL_MENSAJE = f"{URL_TELEGRAM}{TOKEN}/{ENDPOINT}?chat_id={ID_CHAT}&text={TEXTO}"
	consulta = req.get(URL_MENSAJE)

	# URL_MENSAJE = "https://api.telegram.org/bot1842138649:AAGlGHONtm2E0cAR1TYavfY2KPmC4fKlNCo/sendPhoto?chat_id=-559723042&caption=ID%26D"
	# consulta = req.post(URL_MENSAJE, files = imagen)
	
	if (consulta.status_code == 200):
		print("Mensaje enviado")
	else:
		print("ERROR al enviar mensaje")


if (__name__ == "__main__"):
	main()