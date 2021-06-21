clave = "Rodiemigo"
claveCorrecta = False
totalIntentos = 3

for intento in range(1,totalIntentos+1):
    claveIngresada = input("Ingrese Clave:")
    if claveIngresada == clave:
        claveCorrecta = True
        print("Clave Correcta")
        
        break
    else:
        print("Clave incorrecta")
        print(" Intento:", intento, "de ", totalIntentos)
if claveCorrecta == True:
    print("Ingreso Permitido")
else:
    print("Usuario bloqueado")

