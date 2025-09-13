#* Ejercicio

# Con un bucle while, dados dos números enteros proporcionados por el usuario, vamos a encontrar el primer número divisible entre 2, 3 y 5, siempre que sea posible, que se encuentre dentro del intervalo formado por los dos números dados por el usuario (ambos extremos también incluidos).

a = int(input("Introduce el extremo izquierdo del intervalo: "))
b = int(input("Introduce el extremo derecho del intervalo: "))

n = a
while n <= b:
    if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
        print(n)
        break
    n += 1

if n == b + 1:
    print("Dentro del intervalo que has proporcionado, no hay números enteros divisibles entre 2, 3 y 5")

