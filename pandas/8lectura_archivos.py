import pandas as pd

import numpy as np

#leer el archivo 
#delimiter para ver que carcter separar nuestra lectura
#header ponemos desde que linea empezara 
df = pd.read_csv("./pandas-python-master/users.csv",delimiter=",",header=5)

print(df)

#obtener los primeros registros de nuestra dataframe (default 5)

cinco_primeros = df.head(10)

#obtener los ultimos registros de nuestra dataframe (default 5)

cinco_ultimos = df.tail(10)