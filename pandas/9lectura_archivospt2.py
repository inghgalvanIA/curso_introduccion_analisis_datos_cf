import pandas as pd

import numpy as np

#usecols selecionas con que columnas quiero trabajar
#na_values cambiar un valor a NaN
df = pd.read_csv("./pandas-python-master/paises.csv", usecols=["pais", "poblacion", "long", "lat"],na_values=["N/S"])

print(df)

#encontrar los paises que no sean nulos en la poblacion

paisesdf = df[ df.poblacion.notnull() ]

print(paisesdf)

#convertit un int 

paisesdf.apply( lambda row: str(row["poblacion"]).replace("."," ") ,axis=1)

#ordenamiento 1.- indices 2.- columnas

indices = df.sort_index()

print(indices)

#ordenamiento al reves

indices = df.sort_index(ascending=False)

print(indices)

#ordenamiento de columna

colum = df.sort_values("poblacion")

print(colum)