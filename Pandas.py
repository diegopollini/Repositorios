import json
import pandas as pd

RUTA = "datos.csv"
dataFrame = pd.read_csv(RUTA)
print (dataFrame)

#La ruta también podría ser un excel exportado de un Google Sheet