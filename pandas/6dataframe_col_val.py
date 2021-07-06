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

#obtener informacion de nuestro dataframe (columnas)
print(df["nombre"])

#o

print(df.calificaciones)

#obtener informacion de una columna un indice df.columna[fila]

print(df.calificaciones[0])

#con condicionales

print(df.calificaciones[ df.calificaciones > 9])


