from ventas import menu_ventas
from ingresos import (
    registrar_ingreso, 
    calcular_total_ingresos, 
    consultar_ingresos, 
    buscar_ingreso
)
from gastos import menu_gastos
from reportes import (
    contar_palabras,
    contar_lineas,
    contar_caracteres,
    contar_busqueda,
    resumen_completo,
    guardar_resumen,
    verificar_palabra

)


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

def menu_reportes():
    while True:
        print("\nMENU DE ARCHIVOS Y REPORTES")
        print("1. Contar palabras")
        print("2. Contar lineas")
        print("3. Contar caracteres")
        print("4. Buscar coincidencias de una palabra")
        print("5. Mostrar resumen completo")
        print("6. Guardar resumen")
        print("7. Verificar existencia de una palabra")
        print("8. Regresar al menu principal")

        opcion = input("Seleccione una opcion:")

        if opcion == "1":
            contar_palabras()
        elif opcion == "2":
            contar_lineas()
        elif opcion == "3":
            contar_caracteres()
        elif opcion == "4":
            contar_busqueda()
        elif opcion == "5":
            resumen_completo()
        elif opcion == "6":
            guardar_resumen()
        elif opcion == "7":
            verificar_palabra()
        elif opcion == "8":
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
            menu_reportes()
        elif opcion == "5":
            print("\nBUSQUEDA DE REGISTROS")
            buscar_ingreso(ingresos)
        elif opcion == "6":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no valida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()
