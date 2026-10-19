from ventas import menu_ventas
from ingresos import (
    registrar_ingreso, 
    calcular_total_ingresos, 
    consultar_ingresos, 
    buscar_ingreso
)
from gastos import menu_gastos


#Lista para guardar los ingresos durante la ejecucion
ingresos = []


def mostrar_menu():
    print("\n" + "=" * 40)
    print("          SISTEMA DE GESTION")
    print("=" *  40)
    print("1. Gestion de ventas")
    print("2. Gestion de ingresos")
    print("3. Gestion de gastos")
    print("4. Buscar registros")
    print("5. Salir del sistema")
    print("=" * 40)

def menu_ingresos():
    while True:
        print("\nMENU DE INGRESOS")
        print("1. Registrar ingreso")
        print("2. Consultar ingresos")
        print("3. Buscar ingresos")
        print("4. Calcular total de ingresos")
        print("5. Regresar al menu principal")

        opcion = input("Seleccione una opcion:")

        if opcion == "1":
            registrar_ingreso(ingresos)
        elif opcion == "2":
            consultar_ingresos(ingresos)
        elif opcion == "3":
            buscar_ingreso(ingresos)
        elif opcion == "4":
            total = calcular_total_ingresos(ingresos)
            print(f"Total de ingresos: S/ {total}")
        elif opcion == "5":
            break
        else:
            print("Opción no valida.")

def ejecutar_menu():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion:")
        if opcion == "1":
            menu_ventas()
            
        elif opcion == "2":
            menu_ingresos()
        elif opcion == "3":
            menu_gastos()
        elif opcion == "4":
            print("\nBUSQUEDA DE REGISTROS")
            buscar_ingreso(ingresos)
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no valida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()
