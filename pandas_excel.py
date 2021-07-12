# Muestras base de Pandas, dataframes
# https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/export?format=csv
# https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/edit#gid=0

# La librería numpy es muy útil para muchas operaciones de álgebra, Fourier, etc
import numpy as np
import pandas as pd


# RUTA_GSHEETS = "https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/export?format=csv"
RUTA_GSHEETS = "https://docs.google.com/spreadsheets/d/1NpzJARb8qkofgUC0I_rkzun1pmHG7s14tg1M0H11TFY/export?format=xlsx"


def main():
	dataframe = pd.read_excel(RUTA_GSHEETS)
	media = np.mean(dataframe["Puntos"])
	filaMax = np.argmax(dataframe["Puntos"])
	filaMin = np.argmin(dataframe["Puntos"])

	print(dataframe)
	print(media)
	print(filaMax)
	print(filaMin)

	
if (__name__ == "__main__"):
	main()