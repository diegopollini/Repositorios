# Muestras base de Pandas, dataframes
# https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/export?format=csv
# https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/edit#gid=0

import json
import os
import dotenv.main
import pandas as pd
from sqlalchemy import create_engine
import pymysql

# RUTA_LOCAL = "semana11/clasificacion_f1_2021.csv"
# dataframe = pd.read_csv(RUTA_LOCAL)
# print(dataframe)

# RUTA_GSHEETS = "https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/export?format=csv"
# dataframe = pd.read_csv(RUTA_GSHEETS)
# print(dataframe)

# RUTA_GSHEETS = "https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/export?format=xlsx"
# dataframe = pd.read_excel(RUTA_GSHEETS)
# print(dataframe)

MYSQL_SERVIDOR = "pad19.com"
MYSQL_USUARIO = "adimra"
MYSQL_CLAVE = "adm2021"


def conectarMysql():
	motorMysql = create_engine(f"mysql+pymysql://{MYSQL_USUARIO}:{MYSQL_CLAVE}@{MYSQL_SERVIDOR}/adimra_introprog21", pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False

def main():
	conn = conectarMysql()
	if (conn):
		dataframe = pd.read_sql("SELECT * FROM clasificacion_f1", conn)
		print(dataframe)


if (__name__ == "__main__"):
	main()