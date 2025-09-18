# Ejercicio
# Dado un string, con un bucle for vamos a imprimirlo sin vocales y vamos a salir del bucle si la letra que indique el usuario aparece más de n veces, número que también nos proporcionará el usuario.

s = "Pensamos demasiado y sentimos muy poco"

letter = input("Introduce una letra: ")
n = int(input("Indica el máximo número de veces que quieres que aparezca la letra anterior: "))
count = 0 #requerimos un contador que me lleve el número de veces
letter = letter.lower()
s = s.lower()

for c in s:
    if count >= n:
        print("\nSe ha superado el número de apariciones")
        break
    if c == letter:
        count += 1
    elif c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        continue
    print(c, end = "") # para que no se impriman saltos de línea ni espacios en blanco adicionales
    