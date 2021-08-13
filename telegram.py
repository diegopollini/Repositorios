#IFTTT Nexo entre APIs Sitio Web
#https://api.telegram.org/bot1842138649:AAGlGHONtm2E0cAR1TYavfY2KPmC4fKlNCo/getUpdates


import requests as req

def main():
    imagen = {"photo": open("bandera.png","rb")}
    URL_TELEGRAM = "https://api.telegram.org/bot"
    TOKEN = "1724988189:AAHFtLjLLNVhv9aNtKFxoNwlNNKBCcPQogg"
    #ENDPOINT = "sendMessage"
    ENDPOINT = "sendPhoto"
    ID_CHAT = "-577125092"
    TEXTO = "Soy yo probando desde Python"

    #URL_MENSAJE = f"{URL_TELEGRAM}{TOKEN}/{ENDPOINT}?chat_id={ID_CHAT}&text={TEXTO}"
    URL_MENSAJE = f"{URL_TELEGRAM}{TOKEN}/{ENDPOINT}?chat_id={ID_CHAT}&caption=Emocion"
    #consulta = req.get(URL_MENSAJE)
    consulta = req.post(URL_MENSAJE, files = imagen)

    if (consulta.status_code == 200):
        print("Mensaje enviado")
    else:
        print("ERROR al enviar mensaje")

if (__name__=="__main__"):
    main()



#URL_MENSAJE = "https://api.telegram.org/bot1934154895:AAGCBmE0WiEmJUhxWwP22-XmSE0fPxMPBhw/sendMessage?chat_id=-559723042&text=Este es el texto
#consulta = req.get(URL_MENSAJE)

