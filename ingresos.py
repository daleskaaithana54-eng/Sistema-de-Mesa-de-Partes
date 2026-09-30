#Modulo de ingresos

def seleccionar_tipo_ingreso():
    tipos = ["Sueldo", "Venta", "Otros"]
    print("Tipos de ingreso:")
    for i in range(len(tipos)):
        print(i + 1, tipos[i])
    opcion = int(input("Elige un tipo: "))
    return tipos[opcion - 1]


print(seleccionar_tipo_ingreso())