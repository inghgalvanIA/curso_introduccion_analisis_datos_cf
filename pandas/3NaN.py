"""
con la clase NaN representa la ausencia de valor
none
not

"""

import pandas as pd

import numpy as np

#una serie con valores nulos
a = pd.Series ([10,20,np.NaN,40,np.NaN])
print(a)

#para saber si una serie tiene valores 
b = pd.isnull(a)
print(b)

c = pd.notnull
print(c)

d = a.isnull()
print(d)

#eliminar los valores nulos
e= a.dropna()
print(e)

#sustituir los valores nulos por un valor ejempllo 99
f= a.fillna(99)
print(f)

#filtrar con los valores que no son nulos
g = a[a.notnull()]
print(g)