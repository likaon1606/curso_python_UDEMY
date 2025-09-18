# Con un bucle "for", vamos a recorrer un string dado y vamos a imprimir todas las letras salvo por la letra indicada por el usuario

s = "Predecir el futuro resulta ser un negocio muy difícil en sí"

print("El string original es:", s)
letter = input("Introduce la letra que quieras eliminar del string original: ")

s = s.lower()
letter = letter.lower()

for c in s:
    if c == letter:
        continue
    else:
        print(c, end = "") # end es con un final vacío para que los espacios funcionen como espacios