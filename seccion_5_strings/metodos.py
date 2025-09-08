# .lower() *Cambia a minusculas
s = "ME ENCANTA EL CHOCOLATE"
print(s.lower())

# .upper() *Cambia a mayuculas
x = "me encanta el chocolate"
print(x.upper())

# .count() *Cuenta cuantas veces aparece una leta o string dentro de la frase
print(x.count("o")) # es sensible a mayusculas y minusculas

# .capitalize() *Convierte a mayúsculas el primer carácter de un string
print(x.capitalize())

# .title() *Convierte a mayúsculas el primer caracter de cada palabra
print(x.title())

# .swapcase() *Convierte a mayúsculas las minúsculas y viceversa
print(s.swapcase())

# .replace() *Reemplaza el caracter o caracteres que le indiquemos
s = "Los tomberis son buenos"
print(s.replace("buenos", "malos"))

# .split() *rompe el string en el caracter que le indiquemos y elimina dicho caracter
text = "El elefante tiene las orejas muy grandes"
print(text.split("e")) # rompemos por la letra "e" minúscula
print(text.split("tiene")) # rompemos por la palabra "tiene"

# .strip() *elimina los espacios sobrantes a principio y fin
text1 = "       El elefante tiene las orejas muy grandes      s"
print(text1.strip())

# .rstrip() *elimina los espacios sobrantes al final del string
print(text1.rstrip())

# .lstrip() *elimina los espacios sobrantes al principio del string
print(text1.lstrip())

# .find() *busca el caracter que coincida, devolviendo la primer posición encontrada
text3 = "Este es un curso y es de Python"
print(text3.find("es"))

# .index() *Tiene otros 2 parámetros de uso opcional: start y end, que sirven para indicar donde queremos que empiece la búsqueda y donde queremos que acabe
print(text3.index("e", 8)) # solo indicamos "start"
print(text.index("e", 8, 15)) # indicamos start y end

# .rindex() *busca el caracter que indiquemos y devuelve el último índice en el que fué encontrado
print(text3.rindex("e"))