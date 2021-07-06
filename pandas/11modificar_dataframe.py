import pandas as pd

import  numpy as np 

df = pd.DataFrame(np.arange(16).reshape(4,4),columns=list("ABCD"),index=list("abcd") )

print(df)

#remplazar un elemento en particular

df.B["b"] = 50

print(df)

#remplazar la columna completa

df.B = 10,20,30,40

print(df)

#eliminar una columna (genera unn nuevo dataaframe)

df_uno = df.drop("D",axis=1)

print(df_uno)

#agregar una nueva columna
#insert(posicion,nombre,lista valores)
df.insert(1,"z",[100,200,300,400])

print(df)

#o

w = df.assign(w=[100,200,300,400])

print(w)