import requests

RUTA_ARCHIVO_REMOTO = "https://ssl.smn.gob.ar/dpd/observaciones/estadisticas.txt"

contenidoRemoto = requests.get (RUTA_ARCHIVO_REMOTO)
print (contenidoRemoto.status_code)