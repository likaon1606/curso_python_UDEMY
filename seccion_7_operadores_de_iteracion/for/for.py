# Bucle for
# La idea del bucle for es: para todos los elementos de la clave, seguimos realizando las líneas del bucle. Una vez nos quedemos sin elementos, salimos del bucle.

# *Su estructura es la siguiente:

#? for clave:
#   instrucción 1
#   instrucción 2
#   .
#   .
#   .
#   instrucción n

#? s = "Me gustan las matemáticas"

#? for c in s:
#?     print(c)

# Recorrer un string con un ciclo for y devolver impreso del revés

s = "Mi mamá me mima esa es mi mamá"
s_inv = "" # declaramos una variable donde guardaremos el resultado del string al revéss

for c in s:
    s_inv = c + s_inv 

print(s_inv)