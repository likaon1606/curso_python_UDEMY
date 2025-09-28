# El método .pop() devuelve el último elemento de la lista y lo borra de la misma
numbers = [0,1,1,2,2,2,3,4,3,4]

print(numbers)
for i in range(5):
  print(numbers.pop()) #? vamos a popear durante 5 veces los últimos elementos de la lista que va quedando, es decir eliminar los últimos elementos
  print(numbers)
# [0, 1, 1, 2, 2, 2, 3, 4, 3, 4]
# 4
# [0, 1, 1, 2, 2, 2, 3, 4, 3]
# 3
# [0, 1, 1, 2, 2, 2, 3, 4]
# 4
# [0, 1, 1, 2, 2, 2, 3]
# 3
# [0, 1, 1, 2, 2, 2]
# 2
# [0, 1, 1, 2, 2]