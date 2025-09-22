#todo Ejercicio 4
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.

# negativos = 0
# positivos = 0

# n = int(input("Introduce un número porsitivo o negativo (0 para salir): "))

# while n != 0:
#     if n > 0:
#         positivos += 1
#     else:
#         negativos += 1
#     n = int(input("Introduce un número porsitivo o negativo (0 para salir): "))
    
# print("Haz introducido {} números positivos y {} números negativos" .format(positivos, negativos))


#? **** EJEMPLO DEL INSTRUCTOR *****


print("Por favor, introduzca un número entero: ")
number = int(input())
n_pos = 0
total = 0
while number != 0:
    if number > 0:
        n_pos += 1
    total += 1
    number = int(input())
print("De los {} números introducidos, {} son positivos y {} negativos".format(total, n_pos, total - n_pos))