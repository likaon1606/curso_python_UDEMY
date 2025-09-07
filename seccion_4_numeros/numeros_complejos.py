# la letra "j" se reserva para los numeros imaginarios
z = 2 + 5j
print(z)
print(type(z)) # type para saber el tipo

# tambien podemos definir números complejos en Python con la función "complex()"
x = complex(1, -7)
print(x)
print(type(x))

# para obtener la parte real, utilizamos ".real" y para obtener la parte imaginaria usamos ".imag"
print(x.real)
print(x.imag)

# las operaciones son iguales a todas de la forma común
z1 = 2-6j
z2 = 5+4j
print(z1 + z2) # resultado =  (7-2j)
print(z1 - z2) # resultado =  (-3-10j) y así con las demás operaciones...

# para el congujado de un número complejo usamos ".conjugate()"
z3 = -2 + 1j
print(z3.conjugate()) # (-2-1j)

# para calcular el módulo  de un número complejo, utilizamos la función "abs()"
z4 = -2j
print(z4) # (-0-2j)
