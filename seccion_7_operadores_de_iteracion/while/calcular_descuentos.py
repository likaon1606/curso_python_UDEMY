while True:
    categoria = input("Introduce la categoría:\n>>>")

    if categoria.lower() == "cancelar":
        print("Compra cerrada")
        break

    precio = float(input("Introduce el precio del producto:\n>>>"))

    if categoria.lower() == "productos lácteos":
        total = precio * 0.90
        print(f"Descuento de 10%. Por pagar: {total}")
    elif categoria.lower() == "productos horneados":
        total = precio * 0.70
        print(f"Descuento de 30%. Por pagar: {total}")
    else:
        print(f"Sin descuento. Por pagar: {precio}")
