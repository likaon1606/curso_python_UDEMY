# Ejemplo 3
# Vamos a calcular las tablas de multiplicar de los números del 1 al 10 anidando dos bucles for:

for i in range(1, 11):
  print("\nTabla de multiplicar del {}".format(i))
  for j in range(1, 21):
    print("{} x {} = {}".format(i, j, i * j))

