# Repetir strings
s1 = "¡Cumpleaños feliz!"
s2 = "Te deseamos todos"

song = (s1 + "\n") * 2 + s2 + ",\n" + s1
print(song)

# Función str()
nombre = "Ricardo"
numero_gatos = 2

print("Mi abuelo se llama {} y tiene {} gatos" .format(nombre, numero_gatos))