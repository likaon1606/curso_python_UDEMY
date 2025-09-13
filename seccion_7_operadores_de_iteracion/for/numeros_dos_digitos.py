for numero in range(10, 100):  # números de dos dígitos
    decenas = numero // 10     # dígito de las decenas
    unidades = numero % 10     # dígito de las unidades
    producto = decenas * unidades
    doble_producto = 2 * producto

    # Mostrar información de cada número
    print(f"Número: {numero}, dígitos: {decenas} y {unidades}, "
          f"producto: {producto}, doble del producto: {doble_producto}", end='')

    if numero == doble_producto:
        print(" ✅ Cumple la condición")
    else:
        print()
