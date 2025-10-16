# Vamos a multiplicar dos matrices con numpy. Ambas serán proporcionadas por el usuario, así como la dimensión de ambas

#? Nota: Para hacer el producto de 2 matrices, necesitamos que el número de columnas de la primera matriz, coincida con el número de filas de la segunda matriz

import numpy as np

n = int(input("Número de filas de A: ")) 
m = int(input("Número de columnas de A: "))
p = int(input("Número de columnas de B: "))

A = np.empty((n, m)) #primero estará vacia con n filas y m columnas
print("\n=== Matriz A===")
for i in range(n):
    for j in range(m):
        A[i, j] = float(input("Introduce el elemento ({},{})" .format(i, j)))

B = np.empty((m, p)) #primero estará vacia con n filas y m columnas
print("\n=== Matriz B===")
for i in range(m):
    for j in range(p):
        B[i, j] = float(input("Introduce el elemento ({},{})" .format(i, j)))

print("\n=== A * B ===")
print(A.dot(B)) #con el método "dot" multiplica A * B