# Se brinda una base de datos de trabajadores del departamento de marketing. Si el nivel de desempeño de un trabajador está por debajo de 50, se considera de bajo desempeño y se recomienda despedirlo.

#? 1) Escribe una función que identifique a los trabajadores con bajo desempeño. Si se encuentra alguno, se debe mostrar "Se recomienda despedir al trabajador [Nombre]". Luego, se elimina/n de la base de datos.

#? 2) Aplica la función a la base de datos de trabajadores. Luego, muestra los nombres de los empleados restantes en una columna marcada como "Los trabajadores con mejor desempeño:".

staff = {
    'Juan': {
        'cargo': 'marketing',
        'desempeño': 71
    },
    'Sofia': {
        'cargo': 'marketing',
        'desempeño': 65
    },
    'Andres': {
        'cargo': 'marketing',
        'desempeño': 49
    },
    'Romina': {
        'cargo': 'marketing',
        'desempeño': 53
    }
}

# Función que identifica y elimina trabajadores con bajo desempeño
def filtrar_trabajadores(staff_dict):
    # Creamos una lista con los que tienen bajo desempeño (<50)
    despedidos = [nombre for nombre, datos in staff_dict.items() if datos['desempeño'] < 50]

    # Mostramos mensajes de recomendación
    for nombre in despedidos:
        print(f"Se recomienda despedir al trabajador: {nombre}")
        del staff_dict[nombre]  # eliminamos al trabajador del diccionario

# Aplicar la función
filtrar_trabajadores(staff)

# Mostrar los trabajadores restantes
print("Los trabajadores con mejor desempeño:")
for nombre in staff.keys():
    print(nombre)



#? *** VERSIÓN MEJORADA MOSTRANDO EL CARGO Y DESEMPEÑO ***

# Función que identifica y elimina trabajadores con bajo desempeño
def filtrar_trabajadores(staff_dict):
    despedidos = [nombre for nombre, datos in staff_dict.items() if datos['desempeño'] < 50]

    for nombre in despedidos:
        datos = staff_dict[nombre]
        print(f"Se recomienda despedir al trabajador {nombre} - Cargo: {datos['cargo']}, Desempeño: {datos['desempeño']}%")
        del staff_dict[nombre]

# Aplicar la función
filtrar_trabajadores(staff)

# Mostrar trabajadores restantes con cargo y desempeño
print("Los trabajadores con mejor desempeño:")
for nombre, datos in staff.items():
    print(f"{nombre} - Cargo: {datos['cargo']}, Desempeño: {datos['desempeño']}%")
