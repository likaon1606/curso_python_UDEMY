
# Ejercicio 9
# Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos).

# edad = int(input("Introduce tu edad: "))
# año_actual = int(input("Introduce el año actual: "))

# año_nacimiento = año_actual - edad

# print("Los años que has vivido son:")

# for año in range(año_nacimiento, año_actual + 1):
#     print(año)


#? **** EJEMPLO DEL INSTRUCTOR *****

age = int(input("Edad: "))
year = int(input("Año actual: "))
for i in range(year, year - age - 1, -1):
    print(i)
