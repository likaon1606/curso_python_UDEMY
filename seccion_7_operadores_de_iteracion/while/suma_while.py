# Ir sumando los números que el usuario irá ingresando, cuando introduzca 0, saldremos del bucle while. Al salir del bucle, con un "else" mostramos la suma

n = float(input("Introduce un número: "))
sum = 0

while n != 0:
    sum += n
    n = float(input("Introduce un número: "))
else:
    print("La suma total es:", sum)