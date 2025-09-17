# Añadir al programa. Define el método area dentro de la clase para que devuelva el área. El programa debe solicitarle al usuario que ingrese el lado del cuadrado y luego debe mostrar su área.

#? Salida esperada: 
# Ingresa la longitud del lado del cuadrado: 
# >>>3 
# 9

class Square():
    def area(self, side_length):
        return side_length * side_length

figure = Square()
side_length = int(input("Ingresa la longitud del lado del cuadrado: "))
print(figure.area(side_length))


# 🛠️ Clase: Square (el plano del cuadrado)
#     ┌───────────────────────┐
#     │   Métodos / acciones  │
#     │   - area(lado)        │
#     │                       │
#     └───────────────────────┘

# 🔨 Objeto: figure (cuadrado concreto creado)
#     ┌───────────────────────┐
#     │   lado = 3            │  <-- valor ingresado por el usuario
#     │   Métodos heredados   │
#     │   - area()            │
#     └───────────────────────┘

# 🖥️ Llamada al método:
#     figure.area(3)   --> calcula 3 * 3 = 9

# 📄 Resultado mostrado:
#     9


#? 🔹 Otra forma de verlo

# Clase = molde 🏗️
# Define cómo es un cuadrado y qué puede hacer.

# Objeto = instancia 🏠
# Un cuadrado real creado usando el molde. Cada objeto puede tener valores distintos (lado diferente).

# Método = acción ✏️
# Lo que el cuadrado sabe hacer, como calcular su área.

# self = “este objeto específico” 👈
# Permite que cada objeto use sus propios datos.