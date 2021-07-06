import pandas as pd

import numpy as np

#llaves seran las columanas
usuarios = {
    "nombre" : ["Eduardo","Uriel","Marines","Fernando"],
    "calificaciones": [9,10,8.5,9.5],
    "edad": [27,25,30,22],
    "aprobado": [True,True,False,True]
}


data_usuarios = pd.DataFrame(usuarios)

print(data_usuarios)

#cambiar los indices de nuestro dataframe

data_usuarios = pd.DataFrame(usuarios, index=["a","b","c","d"])

print(data_usuarios)

#mandar llamar una columna

print(data_usuarios["nombre"])

#o

print(data_usuarios.nombre)

print(data_usuarios.calificaciones.values)

#conocer las comlumnas de nuestro dateframe
print(data_usuarios.columns)

#conocer los indices de nuestro dateframe
print(data_usuarios.index)

#conocer las dimensiones 
print(data_usuarios)