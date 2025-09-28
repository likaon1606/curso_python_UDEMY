# **Concatenación de listas

#* Dada dos o más listas, podemos concatenarlas haciendo uso de la función "+"
l1 = [True, 21, "Martha"]
l2 = [22.5, False, 22, "Rafa"]
print( l1 + l2 )


# *Repetición de listas
abc = ["A", "B", "C"]
print(abc * 5) # si quiero repetir la lista 5 veces, multiplico la lista por 5
# resultado: ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']

print([0] * 20) # resultado del vector de 20 ceros: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# *crear listas vacías
empty_list = []
print(len(empty_list)) # cero para irla llenado