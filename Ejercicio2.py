import math
edad = int(input("Edad: "))
declaracionJurada = int(input("Declaración jurada: "))

if (edad>18 and declaracionJurada>20000):
    Alicuota = 3500*1.15-3500
    Total = 3500*1.15
    print("Subtotal: $3500")
    print("Aplica alícuota 15%: $", round(Alicuota, 2))
    print("Total a pagar: $", round(Total, 2))
else:
    print("Subtotal: $3500")
    print("No aplica alícuota 15%:")
    print("Total a pagar: $3500")