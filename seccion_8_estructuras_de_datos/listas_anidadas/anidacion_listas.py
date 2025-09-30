# Listas anidadas
# *Las listas anidadas son listas dentro de listas. Es decir, las listas no solo pueden contener números, strings o datos booleanos, sino que también pueden contener otras listas.

#? Ejemplo 1
#* A continuación mostramos una lista anidada, pues consta de 3 elementos:

# * 1 lista de 3 strings
# * 1 lista heterogénea de 3 elementos que a su vez contiene una lista con 5 números
# * 1 número

l = [["María", "Santos", "Fernández"],
     ["Juan", [1, 2, 3, 4, 5], 32], 
     2]
print(l)

# [['María', 'Santos', 'Fernández'], ['Juan', [1, 2, 3, 4, 5], 32], 2]

#? Para acceder a un elemento, necesitamos indicar su índice. Si un elemento está en una lista dentro de una lista dentro de una lista, en primer lugar indicamos el índice de la lista exterior dentro de []; después, el índice de la siguiente lista más exterior también entre []; y por último, el índice de la lista más interna, claramente también entre [].

#* Accedamos al string Fernándezy luego al número 5.

print(l[0][2]) # Fernández
print(l[1][1][4]) # 5