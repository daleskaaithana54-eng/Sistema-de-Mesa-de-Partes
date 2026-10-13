
gastos =[]

def registrar_gasto():
    descripcion = input("Ingrese la descricion del gasto:")
    monto = float(input("Ingrese el monto:"))

    gasto = {
        "descripcion": descripcion,
        "monto": monto
    }

    gastos.append(gasto)

    print("Gasto registrado correctamente.")


def consultar_gastos():
    print("\n--- GASTOS REGISTRADOS ---")

    for gasto in gastos:
        print("Descripcion:", gasto["descripcion"])
        print("Monto: S/", gasto["monto"])

#Modulo de gastos

gastos = []

#Registra un nuevo gasto
def registrar_gasto():
    print("\nREGISTRAR GASTO")
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = float(input("Ingrese el monto del gasto: S/ "))
    while monto <= 0:
        print("El monto debe ser mayor a cero. Intente nuevamente.")
        monto = float(input("Ingrese el monto: S/ "))
    gasto = {"descripcion": descripcion, "monto": monto}
    gastos.append(gasto)
    print("Gasto registrado corectamente.")

#Consultar los gastos registrados
def consultar_gastos():
    print("\nGASTOS REGISTRADOS")
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
    for gasto in gastos:
        print("Descripcion:", gasto["descripcion"])
        print("Monto: S/", gasto["monto"])

#Calcular el total de gastos
def calcular_total_gastos():
    total = 0

    for gasto in gastos:
        total = total + gasto["monto"]
    return total

#Muestra el menu de gastos
def menu_gastos():
    while True:
        print("\nMENU DE GASTOS")
        print("1. Registrar gasto")
        print("2. Consultar gastos")
        print("3. Calcular total de gastos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            consultar_gastos()
        elif opcion == "3":
            total = calcular_total_gastos()
            print("Total de gastos: S/", total)
        elif opcion == "4":
            break
        else:
            print("Opción no valida. Intente nuevamente.")

if __name__ == "__main__":
    menu_gastos()

