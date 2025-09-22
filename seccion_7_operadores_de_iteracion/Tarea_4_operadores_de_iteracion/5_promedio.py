#todo Ejercicio 5
# Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido.

# suma = 0
# contador = 0

# n = int("introduce un número entero o 0 para temrinar programa: ")

# while n != 0:
#     suma += n
#     contador += 1
#     n = int("introduce un número entero o 0 para temrinar programa: ")
# if contador > 0:
#     media = suma / contador
#     print("La media aritmética es:", media)
# else:
#     print("No introdujiste ningún número")


#? **** EJEMPLO DEL INSTRUCTOR *****

number = int(input())
mean = 0
total = 0
while number != 0:
    total += 1
    mean = (mean * (total - 1) + number) / total
    number = int(input())
print("La media aritmética de los números que has introducido es ", mean)