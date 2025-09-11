# Pyratilla hizo un formulario para que los interesados en formar parte de su tripulación rellenaran y así poder evitarse más de una entrevista innecesaria.

# Ahora es momento de filtrar las convocatorias:

# El nombre debe empezar por mayúscula. Si es un nombre compuesto, entonces todos deben empezar por mayúscula.
# La edad debe ser mayor o igual a 16 y menor o igual a 40.
# El hobby indicado debe tener más de 10 caracteres.
# La casilla del sueño no puede haber sido dejada en blanco.
# Ayuda a Pyratilla a crear este filtro para descartar solicitudes que no cumplan estos requisitos.

# Solicitar datos
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
hobby = input("Ingresa tu hobby: ")
sueño = input("Ingresa tu sueño: ")

if not nombre.istitle():
    print("El nombre no cumple (cada palabra debe iniciar con mayúscula).")
elif not (16 <= edad <= 40):
    print("La edad no está en el rango permitido (16-40).")
elif len(hobby) <= 10:
    print("El hobby debe tener más de 10 caracteres.")
elif not sueño.strip():
    print("El campo sueño no puede estar en blanco.")
else:
    print("Solicitud aceptada. ¡Bienvenido a bordo!")

