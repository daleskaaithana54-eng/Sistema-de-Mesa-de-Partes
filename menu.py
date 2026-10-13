from ventas import menu_ventas
from ingresos import registrar_ingreso, calcular_total_ingresos, consultar_ingresos, buscar_ingreso

ingresos = []


def mostrar_menu():
    print("\n" + "=" * 40)
    print("          SISTEMA DE GESTION")
    print("=" *  40)
    print("1. Registrar operaciones de ventas")
    print("2. Calcular total de ingresos")
    print("3. Buscar registros")
    print("4. Leer informacion guardada en archivos y reportes")
    print("5. Salir del sistema")
    print("=" * 40)

def ejecutar_menu():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion:")
        if opcion == "1":
            menu_ventas()
            
        elif opcion == "2":
            while True:
                print("\nMENU DE INGRESOS")
                print("1. Registrar ingreso")
                print("2. Consultar ingresos")
                print("3. Buscar ingresos")
                print("4. Regresar al menu principal")

                opcion_ingreso = input("Seleccione una opcion:")

                if opcion_ingreso == "1":
                    registrar_ingreso(ingresos)
                elif opcion_ingreso == "2":
                    consultar_ingresos(ingresos)
                elif opcion_ingreso == "3":
                    buscar_ingreso(ingresos)
                    
                elif opcion_ingreso == "4":
                    break
                else:
                    print("Opción no valida.")
        elif opcion == "3":
            print("\nBUSQUEDA DE REGISTROS")
            buscar_ingreso(ingresos)
            
        elif opcion == "4":
            print("\nLectura de informacion guardada en archivos y reportes")
            print("Esta opcion se conectara con el modulo de reportes")
            
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            
            break
        else:
            print("\nOpción no valida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()
