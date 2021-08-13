import requests as req
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

SERVIDOR = "pad19.com:3030/productos/10"
USUARIO = "adimra"
CLAVE = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMiLCJub21icmUiOiJhbHVtbm8ifQ.eC452_kHQbCP4wDVvN6nl5Vx8V6HhQP8D5EljApFXS8"
BBDD = "adimra_introprog21"

# Funciones
def conectarMysql():
	motorMysql = create_engine(f"mysql+pymysql://{USUARIO}:{CLAVE}@{SERVIDOR}/{BBDD}", pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False


# Main
if (__name__ == "__main__"):
	resultado = conectarMysql()

	if (resultado):
		print("Conectado a la bbdd, listo para consultas")
	else:
		print("Error al conectar con la bbdd")