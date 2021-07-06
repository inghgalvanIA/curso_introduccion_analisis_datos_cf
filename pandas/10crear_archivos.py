import pandas as pd

import numpy as np

#usecols selecionas con que columnas quiero trabajar
#na_values cambiar un valor a NaN
df = pd.read_csv("./pandas-python-master/paises.csv", usecols=["pais", "poblacion", "long", "lat"],na_values=["N/S"])

#crear un archivo csv

df.to_csv("creado_paises.csv", columns=["pais","poblacion"])