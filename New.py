import requests
URL = "http://api.covid19api.com/summary"
separador = "------------------------------------------------------------------------------------------------------------------------------------------"

def recuperarUrl(destino):
    consulta=requests.get(destino)
    if (consulta.status_code == 200):
        return consulta.json()
    else:
        return False

def main():
    datos = recuperarUrl(URL)
    print("PUNTO 1. SOLICITAR LOS DATOS JSON REMOTOS DESDE CÓDIGO")
    print (datos)
    print(separador)
    print("PUNTO 3. RECUPERAR Y COLOCAR EN DICCIONARIO LOS DATOS DE ARGENTINA")
    miPais = datos["Countries"][6]
    print(miPais)
    print(separador)
    print("PUNTO 4. GUARDAR COPIA DE LOS DATOS DE ARGENTINA EN ARCHIVO JSON LOCAL")
    print("En el directorio raiz se ha creado el archivo datosPais_JSON.txt")
    archivo = open("datosPais_JSON.txt", "w")
    archivo.write(str(miPais))
    archivo.close()
    print(separador)
    print("PUNTO 5. MOSTRAR PARA ARGENTINA:")
    nuevosConfirmados = datos["Countries"][6]["NewConfirmed"]
    totalConfirmados = datos["Countries"][6]["TotalConfirmed"]
    nuevasMuertes = datos["Countries"][6]["NewDeaths"]
    totalMuertes = datos["Countries"][6]["TotalDeaths"]
    nuevosRecuperados = datos["Countries"][6]["NewRecovered"]
    totalRecuperados = datos["Countries"][6]["TotalRecovered"]
    print ("Nuevos Confirmados: ", nuevosConfirmados)
    print ("Total Confirmados: ", totalConfirmados)
    print ("Nuevas Muertes: ", nuevasMuertes)
    print ("Total Muertes: ", totalMuertes)
    print ("Nuevos Recuperados: ", nuevosRecuperados)
    print ("Total Recuperados: ", totalRecuperados)



#FUNCION PRINCIPAL
if (__name__=="__main__"):
    main()