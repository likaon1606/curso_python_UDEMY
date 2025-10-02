# Ejercicio
# Sumas 2 marices con listas. Ambas matrices serán proporcionadas por el usuario, así como la dimensión de las matrices.

n = int(input("Número de filas de las matrices: "))
m = int(input("Número de columnas de las matrices: "))

A = []
print("\n === Matriz A ===")

for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(float(input("Introduce el elemento ({}, {})" .format(i, j))))

B = []
print("\n === Matriz B ===")

for i in range(n):
    B.append([])
    for j in range(m):
        B[i].append(float(input("Introduce el elemento ({}, {})" .format(i, j))))

C = [] # Aquí guardaremos la suma de matrices

for i in range(n):
    C.append([])
    for j in range(m):
        C[i].append(A[i][j] + B[i][j])

print("\n=== Matriz A + B ===") # MOSTRAR DE FORMA BONITA LASW MATRICES
for i in range(n):
    for j in range(m):
        print(C[i][j], end = "  " if C[i][j] >= 0 else " ")
    print("")