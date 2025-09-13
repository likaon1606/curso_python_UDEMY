# Escribe la función perimeter() para calcular el perímetro
def perimeter(lado1, lado2):
    return 2 * (lado1 + lado2)

# Escribe la función area() para calcular el área
def area(lado1, lado2):
    return lado1 * lado2

# Pedir los lados del rectángulo
a = int(input("Ingresa el primer lado del rectángulo:\n>>>"))
b = int(input("Ingresa el segundo lado del rectángulo:\n>>>"))

# Mostrar resultados
print(f"Perímetro = {perimeter(a, b)}")
print(f"Área = {area(a, b)}")

# Ejemplo de uso:
# Ingresa el primer lado del rectángulo:
# >>>2
# Ingresa el segundo lado del rectángulo:
# >>>1
# Perímetro = 6
# Área = 2
