# Dejemos que el usuario decida a quien va dirigida la canción cumpleaños feliz

# método 1
print("Indica el destinatario de la cancion: ")
name = input()

s1 = "¡Cumpleaños feliz!"
s2 = "Te deseamos todos"

song = (s1 + "\n") * 2 + s2.replace("todos", name) + ",\n" + s1
print(song)

