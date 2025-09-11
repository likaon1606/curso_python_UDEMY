# metodos startswith y endswith
s = "Mallorca es una isla preciosa"
print(s.startswith("m")) # false
print(s.endswith("a")) # true
print(s.endswith("bonita")) # false

# método .isalnum() nos da true si todos los caracteres son alfanumericos. Si hay un espacio, marca "false"
x = "Python365" 
print(x.isalnum()) 

# método .isalpha() devuelve verdadero si todos caracteres del string son del alfabeto, si hay espacios marca false
z = "Cachalote"
print(z.isalpha())

# método .isdigit() devuelve true si todos los caracteres son digitos
num = "365"
print(num.isdigit())

# método .isspace() devuelve true si todos los caracteres son espacios en blanco
space = "   "
print(space.isspace())

# método .islower() devuelve true si todos los caracteres son minúsculas aunque haya espacios en blanco
minusculas = "hola como estas"
print(minusculas.islower())

# método .isupper() devuelve true si todos los caracteres son mayúsculas aunque haya espacios en blanco
mayusculas = "HOLA COMO ESTAS"
print(mayusculas.isupper())

#método .istitle() devuelve true si la primer letra de cada palabra del string comienza en mayuscula
titulo = "Hola Como Estas"
print(titulo.istitle())