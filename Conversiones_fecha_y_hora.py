import time

cadenaFecha = "2021-06-28T10:22:00.82Z"
formato = "%Y-%m-%dT%H:%M:%S.82Z"
fecha = time.strptime(cadenaFecha, formato)
fechaConvertida = f"La cadena original {cadenaFecha}, se parsea como {fecha.tm_mday}/{fecha.tm_mon}/{fecha.tm_year} a las {fecha.tm_hour}:{fecha.tm_min}"

print(fechaConvertida)