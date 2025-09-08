# Otras funciones a tener en cuenta
# La función len() nos devuelve el número de caracteres del string.
s = "Tengo hambre"
print(len(s))

# Observación. Los espacios en blanco también son caracteres, por lo que éstos también son incluidos al contar el número de caracteres de los que consta un string.

# Si tenemos un número en formato string, por mucho que sea un número para nosotros, en realidad Python no lo ve así. El gran problema es cuando queremos operar con un número que se encuentra en formato string. Ahí es donde entran en juego las funciones int() y float(), que lo que hacen es convertir a formato integer o float, respectivamente.

numero = "5" 
print(type(numero))
# En este caso, pasamos a formato integer:

numero_int = int(numero)
print(numero_int)

print(numero_int ** 2)

print(type(numero_int))
# En este otro caso, pasamos a formato float:

numero_float = float(numero)
print(numero_float)

print(numero_float ** 2 - numero_float)

print(type(numero_float))
# La función input() sirve para que el usuario introduzca un string por consola:

print("Introduce tu nombre: ")
name = input("Nombre: ")
print(name) 

# Aquí también nos serán útiles las funciones int() y float(), pues si en vez del nombre queremos que el usuario nos indique su edad o su altura, querremos tratar dichos valores como números. Entonces, haríamos lo siguiente
print("Introduce tu edad: ")
age = int(input("Edad: "))
print(age)

print("Introduce tu altura: ")
height = float(input("Altura (en m): "))
print("Introduce tu altura: ")
print(height)

# EJEMPLO COMPLETO
print("La edad de {} es {} y mide {}m".format(name, age, height))


# *Ejercicio: Dado un string, vamos a pedirle al usuario una palabra y vamos a obtener el substring sin la palabra indicada por el usuario usando el método .find() y la función len()

string = "El camino está cerrado pero seguro que podemos encontrar una alternativa"
print("Este es el string original: ", end = "")
print(string)

print("Introduce la palabra que quieras eliminar del string original: ")
word = input("Palabra: ")
idx = string.find(word)
substring = string[:idx] + string[(idx + len(word) + 1):]
print(substring)