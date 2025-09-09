# Vamos a pedir el año de nacimiento al usuario y devolvemos su edad

# print("Introduce tu año de nacimiento: ")
year = int(input("Introduce tu año de nacimiento: "))
this_year = int(input("Introduce el año actual: "))
age = this_year - year

print("En el año {} tienes {} años." .format(this_year, age))