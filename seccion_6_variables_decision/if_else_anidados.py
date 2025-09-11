age = 18
name = "Ariel"

if age >= 18:
    if name.startswith("A") or name.startswith("a"):
        print("Eres mayor de edad y tienes {} años y tu nombre, que es {}, empieza por A".format(age, name))
    else:
        print("Eres mayor de edad pues tienes {} años".format(age))
else:
    print("Eres muy joven")