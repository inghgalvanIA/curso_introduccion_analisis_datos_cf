import pandas as pd

import numpy as np

#llaves seran las columanas
usuarios = {
    "nombre" : ["Eduardo","Uriel","Marines","Fernando"],
    "calificaciones": [9,10,8.5,9.5],
    "edad": [27,25,30,22],
    "aprobado": [True,True,False,True]
}

df = pd.DataFrame(usuarios)

#apply aplicar funciones
#axis=0 recorre por columnas x columna
#axis=1 recorre por filas x fila
#no se actualiza la columna se crea otra
df_uno = df.apply(lambda row: row["edad"] + 1,axis=1)

print(df_uno)

#para actualizar la columna

df.edad = df.apply(lambda row:row["edad"] +1,axis=1)

print(df)