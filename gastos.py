
gastos = []


def registrar_gasto():
    print("\n--- REGISTRAR GASTO ---")

    descripcion = input("Ingrese la descripcion del gasto: ").strip()

    if not descripcion:
        print("Error: la descripcion no puede estar vacia.")
        return

    try:
        monto = float(input("Ingrese el monto: "))

        if monto <= 0:
            print("Error: el monto debe ser mayor que cero.")
            return

    except ValueError:
        print("Error: ingrese un monto numerico valido.")
        return

    gasto = {
        "descripcion": descripcion,
        "monto": monto
    }

    gastos.append(gasto)
    print("Gasto registrado correctamente.")


def consultar_gastos():
    print("\n--- GASTOS REGISTRADOS ---")

    if not gastos:
        print("No hay gastos registrados.")
        return

    total = 0

    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. Descripcion: {gasto['descripcion']}")
        print(f"   Monto: S/ {gasto['monto']:.2f}")
        total += gasto["monto"]

    print(f"\nTotal de gastos: S/ {total:.2f}")
