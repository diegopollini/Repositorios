import pandas as pd
import matplotlib.pyplot as areaGrafica

# datos = pd.read_excel("data.xlsx")
# print(datos.count())

# x = [1, 2, 3, 4]
# y = [2, 4, 8, 16]

# grafico = pd.DataFrame(y, x)
# grafico.plot()

meses = ("Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")
ingresos = [3500, 4200, 3600, 3220, 3300, 1020, 4850, 5000, 4800, 2200, 3500, 3550]

grafico = pd.Series(ingresos, index=meses)
grafico.plot(kind="pie", title="Ingresos por mes")

areaGrafica.show()