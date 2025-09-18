# Comando "continue"

# El comando "continue" es similar a break, pero en vez de salir del bucle, lo que hace es interrumpir la iteración en la que se encuentra y empezar la siguiente iteración.

# Ejemplo 2

# Supongamos que queremos que se nos impriman todos los números entre 0 y 100 que no son ni divisibles entre 2 ni entre 5.

#? Ejercicio. Pensad cómo podríais resolver este problema en el cual se exige que en algún momento utilicéis el comando "continue".

for i in range(101):
  if i % 2 == 0 or i % 5 == 0:
    continue
  print(i)