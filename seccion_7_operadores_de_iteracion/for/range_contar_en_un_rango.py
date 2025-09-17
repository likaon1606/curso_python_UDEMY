# Función range()
#? La función range() tiene 3 posibles argumentos:

# start el numero por el cual comenzaremos a contar, si no lo colocamos, comienza en 9 la cuenta
# stop en donde pararemos
# step el salto, de cuanto en cuanto, por ejemplo: 2 en 2, 3 en 3, etc

for i in range(1, 11, 1):
    print(i) # imprimirá hasta el 10, porque se para un número antes, el "step" podríamos hacerlo en 2 y sería: 1,3,5,7,9 

for x in range(5): # si omitimos el start y el step, comienza el bucle en "0" y el salto con step sería de 1 en 1 por defecto
    print(x)

#? SI QUEREMOS CONTAR AL REVÉS

for i in range(10, 0, -1):
    print(i)