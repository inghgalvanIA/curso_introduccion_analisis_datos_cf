import numpy as np

a = np.random.randint(1,10,10)
c = np.random.randint(0,100,200)

#aquel que cumpla la condicion regresara un True 
res = a < 5
print(res)

#por medio de un arreglo de booleanos regresara solo el valor del indice con True
print(a[res])

print("operdaores logicos")

#numero de elementos 
print(c[(c > 10)].size)

#imprimir solo elementos entra 10 y 50
print("valores entre 10 y 50 con and")
rango = c [(c>10)&(c<50)]
print(rango)

print("valores mayores de 50 o igual a 10 con or")
rango_dos = c[(c>50)|(c == 10)]
print(rango_dos)

print("valores que no sean 50 o igual a 10 con not")
rango_tres = c[(c!=50)|(c < 10)]
print(rango_tres)
