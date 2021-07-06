import pandas as pd

import numpy as np
from pandas.core.indexes.base import Index


usuarios = {
      "nombre" : ["Eduardo","Uriel","Marines","Fernando"],
    "calificaciones": [9,10,8.5,9.5],
    "edad": [27,25,30,22],
    "aprobado": [True,True,False,True]
}

#cuando solo queremos trabajar con ciertas columnas columns=[]
a = pd.DataFrame(usuarios, index=["a","b","c","d"],columns=["nombre","calificaciones"])

#crear una Datafram por medio de una matriz

matriz = np.arange(12).reshape(3,4)

df = pd.DataFrame(matriz, columns=["A","B","C","D"],index=["a","b","c"])

print(df)

#renombrar una columna

df_uno = df.rename(columns={"A":"first"})

print(df_uno)

#rernombrar una fila

df_dos = df.rename(index={"a":"i_uno"})

print(df_dos)