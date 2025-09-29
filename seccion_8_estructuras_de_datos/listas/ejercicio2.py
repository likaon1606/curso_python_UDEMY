# Ejercicio:
# Dada una lista de caracteres, le pedimos al usuario qué elemento quiere eliminar y lo eliminaremos de la lista

l = ["m", "a", "r", "j", "b", "g", "i", "s", "f", "g"]
print("Esta es la lista original", l)
c = input("Introduce el caracter que quieres eliminar: ")

for e in l:
    if e == c:
        l.remove(e)
print(l)