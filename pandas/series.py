import pandas as pd
import numpy as np

#declarar una serie
serie = pd.Series([10,20,30,40,50],dtype=np.integer)

diccionaro = {
    "a":10,
    "b":200,
    "c":3000
}

print(diccionaro)
print(serie)

#obtener el valor de una llave

print(f"el pirmer valor: {serie[0]}")

#obtener el ultimo elemento

print(f"el ultimo valor: {serie.size -1}")

#modificando un valor

serie[0] = 100
print(serie)

#modificar los indices para que sean letras

b = pd.Series([10,20,30,40,50],dtype=np.float32,index=["a","b","c","d","e"])
print(b)

#otener valores por medio d euna lista de subindices
subserie = b[["a","c","d"]]
print(f"una subserie con lista de indices{subserie}")

#crear una serie con un diccionario

c = pd.Series( diccionaro)
print(f"serie creada con un diccionario:  {c}")