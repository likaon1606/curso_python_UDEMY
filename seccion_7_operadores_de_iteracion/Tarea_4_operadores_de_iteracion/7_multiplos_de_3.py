# Ejercicio 7
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
# entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
# el resultado de la suma.

# izquierda = int(input("Introduce el número del extremo izquierdo: "))
# derecha = int(input("Introduce el número del extremo derecho: "))

# suma = 0

# for i in range(izquierda, derecha + 1):
#     if i % 3 == 0:   # si el número es múltiplo de 3
#         suma += i

# print("La suma de los múltiplos de 3 en el intervalo es:", suma)


#? **** EJEMPLO DEL INSTRUCTOR *****

n1 = int(input("Extremo izquierdo: "))
n2 = int(input("Extremo derecho: "))
sum = 0
for i in range(n1, n2 + 1):
    if i % 3 != 0:
        continue
    sum += i
print("La suma asciende a", sum)
