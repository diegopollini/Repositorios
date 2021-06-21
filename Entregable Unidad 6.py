datosIngreso = []
parcial = 0
parcial1 = 0
parcial2 = 0
parcial3 = 0

archivoDatos = open("E:\Curso Fundamentos de Programación\Semana 5\datos.txt", "r")
datosIngreso = archivoDatos.read().split(",")
archivoDatos.close

for indice, item in enumerate(datosIngreso):
    datosIngreso[indice]=int(item)

for i in range (0,182):
    suma =parcial + datosIngreso[i]
    parcial = suma
    i + 1
promedio = suma/182
print("El promedio diario del 1° semestre fue: ", round(promedio))

for j in range (182,365):
    suma1 =parcial1 + datosIngreso[j]
    parcial1 = suma1
    j + 1
promedio1 = suma1/183
print("El promedio diario del 2° semestre fue: ", round(promedio1))

for k in range (0,365):
    suma2 =parcial2 + datosIngreso[k]
    parcial2 = suma2
    k + 1
promedio2 = suma2/365
print("El promedio diario anual fue: ", round(promedio2))

for l in range (0,365):
    if datosIngreso[l] >=8000:
        suma3 = parcial3 + 1
        parcial3 = suma3
    l + 1
porcentaje = (suma3/365)*100
print("La cantidad de días en el año con ingresos mayores o iguales a 8000 es:", suma3)
print("El porcentaje de días con ingresos mayores o iguales a 8000 es: ", round(porcentaje), "%")

datosIngreso.sort()
print("El monto en el día con mayores ingresos en el año fue: ", datosIngreso[0])
print("El monto en el día con menores ingresos en el año fue: ", datosIngreso[364])
