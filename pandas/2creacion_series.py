import pandas as pd
import numpy as np

#creacion de una serie con un array de 0 a 4
a = pd.Series( np.arange(4) )
print(a)

#cambiando los indices por letras
b = pd.Series( np.arange(4), index=["a","b","c","d"] ,dtype=np.float32)

print(b)

# se le puede agregar un nombre de una serie
a.name = "serie_a"
print(a)

#para obtener los indices de una serie
print(a.index)

#para obtener los valores de una serie
print(a.values)

#convertr los indices en una lista
print(a.index.tolist())

a.index.name = "indices"

print(a)

#operaciones con serie

c= a * 10
print(c)

#operadores con serie
d = a[a > 1]
print(d)