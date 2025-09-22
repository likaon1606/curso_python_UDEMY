#todo Ejercicio 2
# *Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la letra o no e indícaselo al usuario por pantalla.

# word = str(input("Introduce una Palabra: "))
# letter = str(input("Introduce una letra: "))

# if word.find(letter):
#     print("Si contiene la letra {}" .format(letter))
# else: 
#     print("No contiene la letra {}" .format(letter))   


#? **** EJEMPLO DEL INSTRUCTOR *****

print("Por favor, introduzca una letra: ")
letter = input()
print("Por favor, introduzca una palabra: ")
word = input()

i = 0
found = False

while i < len(word):
    if word[i] == letter:
        found = True
        break
    i += 1
print("La palabra {} {} contiene la letra {}".format(word,"sí" if found else "no", letter))