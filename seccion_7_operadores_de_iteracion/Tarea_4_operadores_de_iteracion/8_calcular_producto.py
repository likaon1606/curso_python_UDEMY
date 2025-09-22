# Ejercicio 8
# Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
# calcula su producto.

# cantidad = int(input("¿Cuántos números vas a introducir? "))

# producto = 1

# for i in range(cantidad):
#     n = float(input("Introduce un número: "))
#     producto *= n   # multiplicamos el producto por el nuevo número

# print("El producto de todos los números es:", producto)


#? **** EJEMPLO DEL INSTRUCTOR *****

n = int(input("¿Cuántos números vas a introducir? "))
prod = 1
for i in range(n):
    number = int(input())
    prod *= number
print("El prodcuto de los {} números que has introducido es {}".format(n, prod))
