# Ejercicio
# Vamos a pedirle al usuario palabras o frases y le vamos a devolver el mismo string modificado con alguno de los métodos aprendidos según se indique:

# Devolver la palabra en mayúscula
# Devolver la frase con todas las palabras empezando en mayúscula
# Devolver la palabra (con 3 o más letras) con todas las letras en minúscula salvo la tercera letra
# Devolver la palabra con todas las letras en mayúsculas salvo la primera y la última
# Devolver la frase donde cada vez que aparezcan las dos primeras letras de la primera palabra, sean substituidas por cualesquiera otras dos letras.

# Introduce una palabra y yo te la devuelvo en mayúsculas
print("Introduce una palabra y yo te la devuelvo en mayúsculas: ")
word = input()

print(word.upper())


# Introduce una frase y yo te devuelvo todas las palabras empezando en mayúscula
print("Introduce una frase y yo te devuelvo todas las palabras empezando en mayúscula")
s = input()
print(s.title())


# Introduce una palabra con 3 letras o más y yo te devuelvo todas sus letras en minúscula salvo la tercera
print("Introduce una palabra con 3 letras o más y yo te devuelvo todas sus letras en minúscula salvo la tercera")
word = input()
word = word[:2].lower() + word[2].upper() + word[3:].lower()
print(word)


# Introduce una palabra y yo te devuelvo todas sus letras en mayúscula salvo la primera y la última
print("Introduce una palabra y yo te devuelvo todas sus letras en mayúscula salvo la primera y la última")
word = input()
word = word[0].lower() + word[1:(len(word) - 1)].upper() + word[-1].lower()
print(word)

# Introduce una frase y yo te la devuelvo sustituyendo las dos primeras letras de la primera palabra por las letras su

subs = "su"
print("Introduce una frase y yo te la devuelvo sustituyendo las dos primeras letras de la primera palabra por las letras {}".format(subs))
s = input()
print(s.replace(s[:2], subs))

