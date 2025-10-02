# Ejercicio
# *Vamos a introducir manualmente una matriz con "numpy" donde las dimensiones son proporcionadas por el usuario

import numpy as np

n = int(input("número de filas: "))
m = int(input("número de columnas: "))

A = np.empty((n, m))

for i in range(n):
    for j in range(m):
        A[i, j] = float(input("Introduce el elemento ({},{}) " .format(i, j)))

print("\n=== Matriz A ===")
print(A)

# === Matriz A ===
# [[ 1.  0.]
#  [ 0.  2.]
#  [ 1. -1.]]