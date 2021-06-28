import requests

#CONSTANTES
URL_API = "http://api.marketstack.com/v1/eod?access_key=82a116bbb79cd8d96c1b0cf462912d08&symbols=AAPL"

#FUNCIONES
def recuperarUrl(destino):
    consulta=requests.get(destino)
    return consulta.json()

def main():
    cotizaciones = recuperarUrl(URL_API)
    print (cotizaciones)

if (__name__=="__main__"):
    main()