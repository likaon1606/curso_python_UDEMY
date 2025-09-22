# Ejercicio 10
# Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
# lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
# número 5, se deberá mostrar:
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *

# n = int(input("Introduce un número entero: "))

# print("Cuadrado/triángulo 1:")

# # Cuadrado (o rectángulo creciente)
# for i in range(n):
#     for j in range(n + i + 1):   # +1 para que empiece con n+1 asteriscos
#         print("*", end=" ")
#     print()  # salto de línea

# print("\nTriángulo rectángulo:")

# # Triángulo rectángulo
# for i in range(1, n + 2):   # desde 1 hasta n+1
#     for j in range(i):
#         print("*", end=" ")
#     print()

#? **** EJEMPLO DEL INSTRUCTOR *****

n = int(input("Número entero: "))

for i in range(n):
    print("* " * (i + 1) + " " * (20 - (2 * i + 2) + 1) + "* " * n)