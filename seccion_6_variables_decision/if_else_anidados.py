age = int(input("Ingresa tu edad: "))
name = str(input("Ingresa tu nombre: "))
inicial = name[0]

if age >= 18:
    if name.upper().startswith(inicial) or name.lower().startswith(inicial):
        print("Eres mayor de edad y tienes {} años y tu nombre, que es {}, empieza por {}".format(age, name, inicial))
    else:
        print("Eres mayor de edad pues tienes {} años".format(age))
else:
    print("Eres muy joven")