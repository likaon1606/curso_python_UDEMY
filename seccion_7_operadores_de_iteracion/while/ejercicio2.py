# Ejercicio
#? Imaginemos las letras del abecedario ordenadas y dispuestas en círculo. Es decir, a la derecha de la A está la B, luego la C, y así sucesivamente hasta la Z. A la derecha de la Z, se encuentra de nuevo la letra A.

#? Vamos a hacer que el usuario introduzca un valor entero n, que se corresponderá con la rotación que llevará a una determinada letra n posiciones a su derecha. Por ejemplo, si la rotación es 4, entonces la A pasará a la E, la B a la F, ..., la Y a la C y la Z a la D.

#? Con un bucle while, vamos a construir el programa que desplazará las letras n posiciones a la derecha.

# *PISTA: Investiga las funciones chr() y ord() para pasar del valor ASCII de un caracter al caracter y viceversa.

n = int(input("Introduce una rotación: "))
i = 65 # el 65 es el valor ASCII de la "A" por eso iniciamos en ese valor, porque ahí inicia el Abededario con mayúsculas

while i <= 90: # 90 porque es el último valor del abecedario
    if i + n <=90:
        print(chr(i) + ": " + chr(i + n)) #? chr() devuelve el valor en código ASCII
    else:
        print(chr(i) + ": " + chr((i - 26) + n)) # i - 26 regresa a la "A" sea cual sea la diferencia, se vuelve a iniciar el ciclo   
    i += 1