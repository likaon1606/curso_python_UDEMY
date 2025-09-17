# Ejercicio
# Con un bucle for, dada una progresión aritmética de números enteros indicada por el usuario (nos dará el primer término, la diferencia y la cota), vamos a calcular la suma de los elementos incluyendo la cota.

# Un ejemplo de progresión aritmética es: 0, 2, 4, 6, 8, ... donde el primer término es 0 y la diferencia entre sus términos es 2.

a0 = int(input("Introduce el término inicial de una progresión aritmética: "))
d = int(input("Introduce la diferencia de dicha progresión aritmética: "))
af = int(input("Indica la cota para finalizar: "))
sum_an = 0

for an in range(a0, af + 1, d):
    sum_an += an

print("La suma de los términos de la sucesión que has indicado es", sum_an)