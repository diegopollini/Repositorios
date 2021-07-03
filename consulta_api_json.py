import requests

#CONSTANTES
URL_API_CLIMA = "https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&APPID=bbbe84df6ab458740a22a2e0a1eb7663"
#URL_API_CLIMA = "https://ssl.smn.gob.ar/dpd/observaciones/estadisticas.txt"

#FUNCIONES
def recuperarUrl(destino, formato):
    consulta=requests.get(destino)
    if (consulta.status_code == 200):
        if (formato == "original"):
            return consulta.content
        elif (formato == "texto"):
            return consulta.text
        elif (formato == "json"):
            return consulta.json()
        else:
            return False
    else:
        return False

def main():
    infoClima = recuperarUrl(URL_API_CLIMA, "json")
    ciudad = infoClima["list"][0]["name"]
    # Formateo de cadena f'{variable:.1f}' para dejar la variable con un solo decimal
    temperatura = f'{infoClima["list"][0]["main"]["temp"]:.1f}'
    humedad = infoClima["list"][0]["main"]["humidity"]
    #print(f"Ciudad: {ciudad}")
    #print(f"Temperatura {temperatura} °C")
    #print(f"Humedad {humedad} %")
    print (infoClima)
    
#FUNCION PRINCIPAL
if (__name__=="__main__"):
    main()