# coding: utf-8
import numpy as np
lista = [10,20,30,40,50,60]
lista
type(lista)
#creacio del array a partir de una lista
np.array(lista)
#asignar el array a una variable
a = np.array(lista)
type(a)
#atributos
#conocer la cantidad de dimensiones del arreglo
a.ndim
#conocer la cantidad de elementos del arreglo:
a.size
#conocer el tamaño en bits
a.itemsize
#conocer la forma de nuestro arreglo
a.shape
