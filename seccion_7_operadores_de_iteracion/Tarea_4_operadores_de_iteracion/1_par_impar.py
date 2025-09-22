#todo Ejercicio 1
# *Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, muestra si el número introducido es par o impar.

# user = int(input("Introduce solo números enteros o 0 para salir: "))

# while user > 0:
#     if user % 2 == 0:
#         print("El número es par")
#     else:
#         print("El número es impar")

#     user = int(input("Introduce solo números enteros o 0 para salir: "))
# else:
#     print("Has salido del programa")


#? **** EJEMPLO DEL INSTRUCTOR *****

print("Introduzca un número entero: ")
number = int(input())

while number != 0:
    print("El número {} es {}" .format(number, "par" if number % 2 == 0 else "impar"))
    number = int(input())

print("Has salido del bucle")
