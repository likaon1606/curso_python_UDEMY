# Podemos combinar un bucle "while" con el operador "else" para ejecutar un bloque de código, una vez la condición del "while" haya dejado de ser verdadera

i = 10
print("Preparados para despegue. Empieza la cuenta atrás")

while i >= 0:
    print(i)
    i -= 1
else:
    print("La cuenta atrás ha finalizado.")