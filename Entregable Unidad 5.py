import random
data= []
i = 0
cantMuestras = 10
minHorno = 100
maxHorno = 200

while (True):
    temperatura=random.randint(minHorno,maxHorno)
    print("Temperatura actual: ",temperatura, "°C")
    temperaturaPrueba = int(input("Ingrese temperatura de prueba entre 100°C - 200 °C: "))
    if (temperaturaPrueba > minHorno and temperaturaPrueba < maxHorno):
        for i in range (0,cantMuestras):
            i+1
            data.append(random.randint(temperatura-2, temperatura+2))
        print("Lecturas instantáneas del sensor: ", (data))
        suma = sum(data)
        print("La suma de todas las mediciones es: ", suma)
        print("La cantidad de muestras tomadas es: ", cantMuestras)
        promedio=round(suma/cantMuestras,2)
        print("El promedio de las temperaturas tomadas por el sensor es: ", promedio)
        data.clear()
        if (promedio < temperaturaPrueba-2):
            print("Temperatura baja, se enciende quemador")
            print("----------------------------------------------------------------------------------------")
        elif ((promedio>=temperaturaPrueba-2) and (promedio<=temperaturaPrueba+2)):
            print("Horno estable")
            print("----------------------------------------------------------------------------------------")
        elif (promedio > temperaturaPrueba+2):
            print("Temperatura alta, se apaga quemador")
            print("---------------------------------------------------------------------------------------")
    elif (temperaturaPrueba == 0):
        print("FIN")
        break
    else:
        print ("ERROR! Ingrese una valor dentro del rango")
        print("-------------------------------------------------------------------------------------------")
