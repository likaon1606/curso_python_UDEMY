# *** Tarea 5 - Estructuras de datos: Listas ***

# Ejercicio 1
# Crea un programa que lea una secuencia de caracteres, guarde cada caracter en una posición de una lista y
# finalmente muestre la secuencia invertida.

secuencia = input("Ingresa una secuencia de caracteres: ")

guardar_lista = []

for c in secuencia:
    guardar_lista.append(c)
guardar_lista.reverse()

print(''.join(guardar_lista))

#? Una forma más simple:

# # Leer una secuencia de caracteres
# secuencia = input("Ingresa una secuencia de caracteres: ")

# # Guardar cada caracter en una lista
# lista_caracteres = list(secuencia)
# # Invertir la lista
# lista_invertida = lista_caracteres[::-1]
# print("Secuencia invertida:", ''.join(lista_invertida))



# *Ejercicio 2
# Crea un programa que lea dos strings de la misma longitud, los guarde intercalados en una lista. Por último,
# mostrar el contenido de la lista.
# Por ejemplo, si introducimos hola caracola y adios marieta, debería mostrarse haodleao sc
# amraarcioeltaa.

cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

if len(cadena1) != len(cadena2):
    print("Error: Las cadenas deben tener la misma longitud.")
else:
    # Intercalar los caracteres de ambas cadenas
    lista_intercalada = []
    for i in range(len(cadena1)):
        lista_intercalada.append(cadena1[i])
        lista_intercalada.append(cadena2[i])
    
    print("Contenido de la lista:", ''.join(lista_intercalada))


#? SOLUCION DEL PROFESOR:

# s1 = input("Introduce el primer string: ")
# s2 = input("Introduce el segundo string: ")
# l = []

# if len(s1) == len(s2):
#     for i in range(len(s1)):
#         l.append(s1[i])
#         l.append(s2[i])
#     for item in l:
#         print(item, end = "")
# else:
#     print("Los strings no tienen el mismo tamaño")


# Ejercicio 3
# Crea un programa que lea un string y guarde en una lista todas las consonantes.

# Leer un string
texto = input("Ingresa un String: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Crear una lista solo con las consonantes
consonantes = [letra for letra in texto if letra.isalpha() and letra not in vocales] # .isalpha asegura que solo se consideren letras(ignora espacios o simbolos)

# Mostrar la lista de consonantes
print("Consonantes encontradas:", consonantes)


#? SOLUCION DEL PROFESOR:

# string = input("Introduce un string: ")
# listaString = []

# for c in string.lower():
#     if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
#         continue
#     listaString.append(c)
# print("Consonantes: ",listaString)


# Ejercicio 4
# Crea un programa que lea una palabra, la guarde en una lista y compruebe si se trata de un palíndromo.




# Ejercicio 5
# Crea un programa que lea una matriz 3 x 3 y devuelva el máximo de cada fila.


# Ejercicio 6
# Crea un programa que lea un entero, n, de teclado y construya una matriz de tamaño n × n. Cada posición
# debe contener su orden en la matriz (desde 0 hasta n2 − 1. Por ejemplo, si n es 3, deberá crearse la matriz
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]



# Ejercicio 7
# Crea una matriz de n × m y asigna los valores manualmente. El programa debe indicar si la suma de cada
# columna es el mismo valor.




# Ejercicio 8
# Crear un programa determina si la matriz introducida manualmente (tanto sus dimensiones como los elementos)
# se trata de la matriz identidad. Recuerda que la matriz identidad debe ser una matriz cuadrada.




# Ejercicio 9
# Realiza un programa que calcule la matriz transpuesta.




# Ejercicio 10
# Crea un programa que pida al usuario la dimensión y cree la matriz identidad de orden correspondiente con
# numpy.