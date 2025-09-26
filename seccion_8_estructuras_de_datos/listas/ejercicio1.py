# Ejercicio

# Vamos a pedirle al usuario la longitud de una lista y haremos que introduzca por teclado tantos números enteros como haya indicado, que se guardarán en una lista. Al acabar, imprimiremos la lista.  

n = int(input("Introduce la cantidad de elementos para tu lista: "))
nums = []

for i in range(n):
    nums.append(int(input()))
print("Tu lista es: ", nums)