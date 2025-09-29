# Ejercicio
# Vamos a pedir al usuario que ingrese 10 números, los guardaremos en una lista y mostraremos la lista ordenada, siendo el usuario quien indique el orden: ascendente o descendente.

reversed = bool(input("Si quieres orden descendente, escribe True. De lo contrario, dale a la tecla Enter: "))
l = []

for _ in range(10): # con el "_" no guardamos la variable
    l.append(float(input()))

l.sort(reverse = reversed)
print(l)