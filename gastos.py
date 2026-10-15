

# Modulo de gestion de gastos

gastos = []


def registrar_gasto():
    print("\n--- REGISTRAR GASTO ---")

    descripcion = input("Ingrese la descripcion del gasto: ").strip()

    if not descripcion:
        print("Error: la descripcion no puede estar vacia.")
        return

    try:
        monto = float(input("Ingrese el monto del gasto: S/ "))

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

    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. Descripcion: {gasto['descripcion']}")
        print(f"   Monto: S/ {gasto['monto']:.2f}")

    print(f"Total de gastos: S/ {calcular_total_gastos():.2f}")


def calcular_total_gastos():
    total = 0

    for gasto in gastos:
        total += gasto["monto"]

    return total


def menu_gastos():
    while True:
        print("\n--- MENU DE GASTOS ---")
        print("1. Registrar gasto")
        print("2. Consultar gastos")
        print("3. Calcular total de gastos")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            consultar_gastos()
        elif opcion == "3":
            print(
                f"Total de gastos: S/ "
                f"{calcular_total_gastos():.2f}"
            )
        elif opcion == "4":
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    menu_gastos()
