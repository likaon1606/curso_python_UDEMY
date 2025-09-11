# Realizar un programa que resuelva ecuaciones de primer grado de la forma Ax + B = 0 proporcionadas por el usuario donde A != 0

A = float(input("Coeficiente A = ")) #AMBOS A Y B serán numeros realez que el usuario va a introducir po pantalla
B = float(input("Coeficiente B = "))

if A != 0:
    sol = -B / A
    print("La solución es x = ", sol)
else:
    print("No hay ecuación que resolver, porque A es = 0")