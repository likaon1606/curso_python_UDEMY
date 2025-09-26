l = [1,2,3,4,5,6,]
print(l)
print(l[-1]) #ultimo elemento
print(l[:3]) # del inicio hasta la posicion 3
print(l[4:]) # posicion 4 hasta el final

names = ["Miguel", "Ariel", "Jorge"]
print(names)
print(names[1])
print(names[-3]) # tercer elemento empezando por el final
print(names[1:3]) # con los : accedemos a un rango de posiciones

#? MODIFICAR listas de manera simple

names[0] = "Alexa"
names[2] = "Naty"
print(names)


#? Añadir elementos a listas

# * Con el método .append() podemos añadir elementos al final de la lista
names2 = ["Juana", "Alexa", "Tita"]
print(names2)

names2.append("Andrea")
names2.append("Sofía")
print(names2)


# * Con el método .insert() podemos añadir elementos en una posición específica
#!NOTA: cada vez que insertamos un valor, el valor de esa poisción se mueve una posición adelante, si "Juan" tiene la posicón 1 y se inserta un valor en esa posición "Juan" tendrá la posición 2 ahora y así suce

names2.insert(1, "David")
print(names2)
names2.insert(3, "Goliat")
print(names2)
