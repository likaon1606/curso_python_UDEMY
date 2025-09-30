# Matrices
# *Hay un tipo muy utilizado de listas anidadas. Se caracteriza por ser una lista de  m  listas, donde cada una de las listas tiene el mismo número de elementos,  n . A este tipo de listas se les conoce como matrices.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix))
# <class 'list'>

# En matemáticas, las matrices se definen del siguiente modo.

# Matriz. Una matriz de dimensiones  m×n  es una tabla formada por elementos dispuestos en  m  filas y  n  columnas de la forma


# A = ⎛a11  a12 ... a1n  ⎞
#     ⎜a21  a22 ... a2n   ⎜ 
#     ⎜ .    .  .     .   ⎜
#     ⎜ .    .   .    .   ⎜
#     ⎜ .    .    .   .      
#     ⎜am1  am2 ... amn  ⎠


# Los elementos de la matriz se representan con doble subíndice,  aij , donde el primero indica la fila a la que pertenece y, el segundo, la columna.

# Entonces, la matriz que hemos definido anteriormente
print(matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

                                              # 1 2 3
# escrita en forma de tabla sería: matrix  =    4 5 6
                                              # 7 8 9
                                                  
# Para acceder a los elementos de una matriz en Python, utilizamos la sintaxis [][], donde primero indicamos la fila y, a continuación, la columna

print(matrix[0][2]) # 3 el primer corchete indica la fila y el segundo la columna
print(matrix[1][1]) # 5
print(matrix[2][0]) # 7

#? Podemos mostrar una matriz de Python en forma de tabla con un bucle for, del siguiente modo

for row in matrix: # Accedemos a las filas de la matrix
    print(row)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# *Si lo que queremos es mostrar todos los elementos de la matriz en columna, podemos utilizar dos bucles for anidados del siguiente modo:

for row in matrix: # Accedemos a las filas
    for element in row: # Accedemos a los elementos de las filas
        print(element)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


#? Si lo que queremos es mostrar la matriz en forma de tabla, sin comas ni claudators por en medio, lo podemos hacer de dos formas:

# *Haciendo uso de las dimensiones de la matriz y, por tanto, de la función range()
# *Sin hacer uso de las dimensiones
# *La primera forma sería:

# m es el número de filas y n, el de columnas
m = len(matrix)
n = len(matrix[0])

for i in range(m):
  for j in range(n):
    print(matrix[i][j], end = " ") # end sirve para colcoar un espacio en blanco y separar los elementos
  print("") # print vacío al final, es como un salto de línea o un ENTER

# 1 2 3 
# 4 5 6 
# 7 8 9 

#! Observación.

# *Como todas las filas tienen el mismo número de elementos, nos da igual si calculamos  n  con la primera fila o con cualquier otra.

# *Hemos hecho uso del parámetro end de la función print() para indicar si, en vez de un salto de línea como ocurre por defecto, queremos que suceda otra cosa inmediatamente después de ejecutar la función print(). En este caso, hemos indicado que queremos un espacio en blanco.


#? Y la segunda forma, es la siguiente:

for row in matrix:
    for element in row:
        print(element, end = " ")
    print("")

# 1 2 3 
# 4 5 6 
# 7 8 9 



# ? ***************** Suma de matrices **********************

# *Para poder sumar dos matrices, necesitamos que tengan la misma dimensión. 

# Dadas dos matrices con la misma dimensión, las podemos usar haciendo uso de bucles `for` anidados.

A = [[1, 0, -3], [2, 0, 1], [-1, -1, 0]]
B = [[-1, -2, 0], [-2, 3, 0], [0, 0, -3]]

m = len(A)
n = len(A[0])

if len(A) == len(B) and len(A[0]) == len(B[0]):
    C = []

    for i in range(m):
        C.append([])
        for j in range(n):
          C[i].append(A[i][j] + B[i][j])

    print(C)

else:
    print("No se puede realizar la suma, pues las dimensiones de las matrices no coinciden.")

# [[0, -2, -3], [0, 3, 1], [-1, -1, -3]]



#? El resultado de sumar las matrices  A  y  B  ha sido

for row in C:
    print(row)

# [0, -2, -3]
# [0, 3, 1]
# [-1, -1, -3]

#! Observación. Hemos puesto un if que, suponiendo que tanto  A  como  B  son matrices, comprueba si sus dimensiones coinciden. De ser cierto, procede a hacer la suma. De lo contrario, devuelve un mensaje indicando que la suma no puede llevarse a cabo


#? Producto de matrices
# *Para poder multiplicar matrices, necesitamos que la matriz de la izquierda tenga el mismo número de columnas que número de filas tiene la matriz de la derecha.

# Dadas dos matrices, la primera con el mismo número de columnas que filas tiene la segunda, podemos multiplicarlas del siguiente modo:

D = [[1, 0, -3, 2], [2, 0, 1, 1], [-1, 0, -1, 0]]
E = [[-1, -2, 0], [-2, 3, 0], [0, 0, -3], [1, 1, -1]]

m1, n1, p1 = len(D), len(E), len(E[0])

F = []

for i in range(m1):
  F.append([])
  for j in range(p1):
    elemento = 0
    for k in range(n1):
      elemento = elemento + D[i][k] * E[k][j]
    F[i].append(elemento)
    print(F)

# RESULTADO DE FILAS
for row in F:
    print(row)

#[1, 0, 7]
# [-1, -3, -4]
# [1, 2, 3]