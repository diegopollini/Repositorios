import requests
import time

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
    print("PUNTO 2. RECUPERAR LA FECHA DE LA ULTIMA ACTUALIZACIÓN")
    cadenaFecha = datos["Global"]["Date"]
    #print (cadenaFecha)
    cadenaFechaRecortada = cadenaFecha[0:19]
    #print (cadenaFechaRecortada)
    formato = "%Y-%m-%dT%H:%M:%S"
    fecha = time.strptime(cadenaFechaRecortada, formato)
    fechaFormateada = f"Ultima actualización: {fecha.tm_mday}/{fecha.tm_mon}/{fecha.tm_year} a las {fecha.tm_hour}:{fecha.tm_min}:{fecha.tm_sec}"
    print (fechaFormateada)
    print (separador)
    print("PUNTO 3. RECUPERAR Y COLOCAR EN DICCIONARIO LOS DATOS DE ARGENTINA")
    miPais = datos["Countries"][6]
    print(miPais) #Imprime el dictionario con los datos de Argentina
    print(separador)
    print("PUNTO 4. GUARDAR COPIA DE LOS DATOS DE ARGENTINA EN ARCHIVO JSON LOCAL")
    print("En el directorio raiz se ha creado el archivo datosPais_JSON.txt")
    archivo = open("datosPais_JSON.txt", "w")
    archivo.write(str(miPais)) #Escribe el archivo con los datos de Argentina en formato JSON
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
    print(separador)
    print("PUNTO 6. CALCULAR EL % DE TOTAL CONFIRMADOS Y TOTAL RECUPERADOS DE ARGENTINA, EN BASE A LOS DATOS GENERALES (GLOBAL)")
    totalConfirmadosGlobal = datos["Global"]["TotalConfirmed"]
    totalRecuperadosGlobal = datos["Global"]["TotalRecovered"]
    print ("Total Confirmados en el mundo: ",totalConfirmadosGlobal)
    print ("Total Recuperados en ele mundo: ",totalRecuperadosGlobal)
    porcentajeTotalConfirmados = f'{totalConfirmados/totalConfirmadosGlobal*100:.2f}'
    porcentajeTotalRecuperados = f'{totalRecuperados/totalRecuperadosGlobal*100:.2f}'
    print ("Porcentaje Total Confirmados en Argentina: ", porcentajeTotalConfirmados, "%")
    print ("Porcentaje Total Recuperados en Argentina: ", porcentajeTotalRecuperados, "%")


#FUNCION PRINCIPAL
if (__name__=="__main__"):
    main()