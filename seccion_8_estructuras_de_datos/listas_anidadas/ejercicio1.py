# Ejercicio
# *Vamos a convertir los números impares del 0 al 30 a una lista y mostrar los elementos con el formato "El valor {} ocupa el índice {}"

odd = list(range(1, 30, 2))

for i in range(len(odd)):
    print("El valor {} ocupa el índice {}" .format(odd[i], i))

# El valor 1 ocupa el índice 0
# El valor 3 ocupa el índice 1
# El valor 5 ocupa el índice 2
# El valor 7 ocupa el índice 3
# El valor 9 ocupa el índice 4
# El valor 11 ocupa el índice 5
# El valor 13 ocupa el índice 6
# El valor 15 ocupa el índice 7
# El valor 17 ocupa el índice 8
# El valor 19 ocupa el índice 9
# El valor 21 ocupa el índice 10
# El valor 23 ocupa el índice 11
# El valor 25 ocupa el índice 12
# El valor 27 ocupa el índice 13
# El valor 29 ocupa el índice 14