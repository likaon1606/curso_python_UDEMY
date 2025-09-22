
#todo Ejercicio 3
# Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario.

# presupuesto = 200
# total = 0

# precio = int(input("Introduce un precio (0 para terminar programa): "))

# while precio != 0 and total + precio <= presupuesto:
#     total += precio
#     precio = int(input("Introduce un precio (0 para terminar programa): "))
# if precio == 0:
#     print("Se terminó de ingresar precios")
# else:
#     print("No puedes ingresar esa cantidad, te pasas del presupuesto")

# print("El total gastado es:", total, "€")  


#? **** EJEMPLO DEL INSTRUCTOR *****


print("Por favor, introduzca un precio: ")
number = float(input())
total = number
while number != 0:
    if total >= 200:
        break
    number = float(input())
    total += number
if total > 200:
    print("No tienes presupuesto")
else:
    print("El total asciende a", total)