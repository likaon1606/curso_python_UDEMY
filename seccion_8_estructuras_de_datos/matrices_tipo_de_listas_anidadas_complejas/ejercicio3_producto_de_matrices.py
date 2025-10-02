# Ejercicio
# Calcular el producto de dos matrices con listar. Ambas matrices serán dadas por el usuario, así como las dimensiones de ambas.

n = int(input("Número de filas de la matriz A: "))
m = int(input("Número de colmnas de la matriz A: ")) 
p = int(input("Número de colmnas de la matriz B: ")) #! para que A Y B puedan multiplicarse, el número de columnas de A, deben coincidir con el número de filas de B

# *Creamos la matriz A
A = []
print("\n=== Matriz A ===")

for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(float(input("Introduce el elemento ({},{})" .format(i, j))))

# *Creamos la matriz B
B = []
print("\n=== Matriz B ===")

for i in range(m): # recordemos que B tiene "m" filas y "p" columnas
    B.append([])
    for j in range(p):
        B[i].append(float(input("Introduce el elemento ({},{})" .format(i, j))))

# *Creamos la matriz "P" del producto resultante de las matrices A * B
C = []

for i in range(n):
    C.append([])
    for j in range(p):
        elemento = 0
        for k in range(m):
            elemento += A[i][k] * B[k][j]
        C[i].append(elemento)

# *mostrar el producto
print("\n=== Matriz A * B ===")
for i in range(n):
    for j in range(p):
        print(C[i][j], end = "  " if C[i][j] >=0 else " ")
    print("")
