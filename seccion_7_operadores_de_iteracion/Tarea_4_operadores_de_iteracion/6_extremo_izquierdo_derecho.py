# Ejercicio 6
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
# números introducidos por el usuario (los extremos incluidos).

# izquierda = int(input("Introduce el número del extremo izquierdo: "))
# derecha = int(input("Introduce el número del extremo derecho: "))

# print("Los números en el intervalo son:")

# for i in range(izquierda, derecha + 1):
#     print(i)


#? **** EJEMPLO DEL INSTRUCTOR *****

n1 = int(input("Extremo izquierdo: "))
n2 = int(input("Extremo derecho: "))
for i in range(n1, n2 + 1):
    print(i)
