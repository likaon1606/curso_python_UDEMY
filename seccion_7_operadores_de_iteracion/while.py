# inicialización de la variable de la condición
# while condición verdadera:
#   instrucción 1
#   instrucción 2
#   .
#   .
#   .
#   instrucción n

i = 1 # inicializamos la variable
while i <= 10: # queremos que i como mucho valga 10
    print(i) #imprimimos los números
    i += 1 # incrementamos una unidad en cada iteración


#***** Cortar el bucle while con "break"  ******

# Supongamos que queremos que se nos impriman los 20 primeros términos de esta serie. Por tanto, necesitaremos por un lado los términos de la serie y, por otro, los índices que ocupan.

fibo_ant = 1 # Término anterior
fibo = 1 # Término actual
idx = 3 # Como ya tenemos los dos primeros términos, empezamos con el índice 3

print("El término {} ocupa la posición {}".format(fibo_ant, 1))
print("El término {} ocupa la posición {}".format(fibo, 2))

while fibo <= 500000: # Establecemos una cota para que el bucle no sea infinito
  temp = fibo  # Guardamos temporalmente el fibonacci actual 
  fibo = fibo + fibo_ant  # Calculamos el nuevo término de la sucesión
  fibo_ant = temp # Modicamos el valor del término anterior
  
  print("El término {} ocupa la posición {}".format(fibo, idx))
  
  if idx == 20: # Si llegamos al vigésimo índice, 
    break       # salimos del bucle
  
  idx += 1 # Incrementamos el valor del índice