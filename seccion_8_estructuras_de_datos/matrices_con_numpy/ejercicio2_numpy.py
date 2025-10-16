# Vamos a sumar dos matrices con numpy. Ambas matrices las proporcionará el usuario, así como sus dimensiones.

import numpy as np

n = int(input("Número de filas: "))
m = int(input("Número de columnas: "))

A = np.empty((n, m))
print("\n=== Matriz A ===")
for i in range(n): #número de filas
    for j in range(m): #número de columnas
        A[i, j] = float(input("Introduce el elemento ({},{})" .format(i, j)))

B = np.empty((n, m))
print("\n=== Matriz B ===")
for i in range(n): #número de filas
    for j in range(m): #número de columnas
        B[i, j] = float(input("Introduce el elemento ({},{})" .format(i, j)))

print("\=== Matriz A + B ===")
print(A + B) #MOSTRAR EL RESULTADO
