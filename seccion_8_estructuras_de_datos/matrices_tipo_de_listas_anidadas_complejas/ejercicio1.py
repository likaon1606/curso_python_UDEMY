# Ejercicio

# *Vamos a crear una matriz de tamaño 4 x 4 y guardarla en una lista.

A = []

for i in range(4):
    A.append([])
    for j in range(4):
        A[i].append(float(input("Introduce el elemento ({}, {}: )" .format(i, j))))
for i in range(4):
    for j in range(4):
        print(A[i][j], end = "  " if A[i][j] >= 0 else " ")
    print("")