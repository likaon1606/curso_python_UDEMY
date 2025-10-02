# Matrices con numpy
# *Existe una forma más sencilla de trabajar con matricdes y es gracias a la librería numpy. Para importarla, simplemente hay que ejecutar la siguiente línea de código.

# import numpy as np

#? *Para crear una matriz vacía, usamos el método .empty(), al que le indicamos por parámetro las dimensiones
import numpy as np

A = np.empty((2, 3)) # tendrá 2 filas y 3 columnas
print(A)

# [[6.23042070e-307 3.56043053e-307 1.37961641e-306]
#  [1.05695167e-307 8.01097889e-307 1.24611470e-306]]


#? *Para crear una matriz vacía con las mismas dimensiones de otra matriz definida anteriormente, usamos el método .empty_like(), al que le indicamos por parámetro la matriz existente

B = np.empty_like(A) # también tendrá 2 filas y 3 columnas
print(B)

#[[6.23042070e-307 3.56043053e-307 1.37961641e-306]
#  [1.05695167e-307 8.01097889e-307 1.24611470e-306]]


#? *Para crear una matriz nula, usamos el método .zeros(), al que le indicamos por parámetro las dimensiones. Una matriz nula es cuando tiene cero en todas sus posiciones, aquí SÍ se asingan ceros, a diferencia de A y B que so vacías

C = np.zeros((3, 5)) # Matriz nula de dimenciones 3 x 5
print(C)

#[[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]


#? *Para crear una matriz de ceros con las mismas dimensiones de otra matriz definida anteriormente, usamos el método .zeros_like(), al que le indicamos por parámetro la matriz existente

D = np.zeros_like(A) # Tendrá 2 filas y 3 columnas y todos sus elementos valdrán 0
print(D)

# [[0. 0. 0.]
#  [0. 0. 0.]]

#? *Para crear una matriz de unos, usamos el método .ones(), al que le indicamos por parámetro las dimensiones

E = np.ones((1, 4)) # Matriz de unos de dimensiones 1 x 4
print(E)

# [[1. 1. 1. 1.]]


#? *Para crear una matriz de unos con las mismas dimensiones de otra matriz definida anteriormente, usamos el método .ones_like(), al que le indicamos por parámetro la matriz existente

F = np.ones_like(C) # Tendrá 3 filas y 5 columnas y todos sus elementos valdrán 1
print(F)

# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]


#? *Podemos crear matrices de numpy a partir de listas con el método .matrix()

M = np.matrix([[1, 0, -3, 2], [2, 0, 1, 1], [-1, 0, -1, 0]])
print(M)

# [[ 1  0 -3  2]
#  [ 2  0  1  1]
#  [-1  0 -1  0]]

#? *Para saber las dimensiones de una matriz, podemos utilizar el método .shape, va sin parentésis

print(M.shape)
# (3, 4) 3 filas y 4 columnas en M


#? *Ahora es más sencillo sumar matrices, pues solamente necesitamos la función +

A = np.matrix([[1, 0, -3], [2, 0, 1], [-1, -1, 0]])
B = np.matrix([[-1, -2, 0], [-2, 3, 0], [0, 0, -3]])

matrixSum = A + B
print(matrixSum)

# [[ 0 -2 -3]
#  [ 0  3  1]
#  [-1 -1 -3]]


#? *También es más sencillo hacer el producto matricial  A⋅B  con el método .dot(). Esto es en lugar del "*" para poder multiplciar y saar el producto de las matrices A Y B

A = np.matrix([[1, 0, -3, 2], [2, 0, 1, 1], [-1, 0, -1, 0]])
B = np.matrix([[-1, -2, 0], [-2, 3, 0], [0, 0, -3], [1, 1, -1]])

matrixProd = A.dot(B)
print(matrixProd)

# [[ 1  0  7]
#  [-1 -3 -4]
#  [ 1  2  3]]


#? *Gracias a numpy, también es mucho más sencillo mostrar una matriz en forma de tabla, pues nos basta con hacer uso de la función print():

print(matrixSum)
print(matrixProd)

# [[ 0 -2 -3]
#  [ 0  3  1]
#  [-1 -1 -3]]

# [[ 1  0  7]
#  [-1 -3 -4]
#  [ 1  2  3]]