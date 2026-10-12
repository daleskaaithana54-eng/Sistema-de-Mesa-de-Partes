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
            print("\nRegistro de operaciones de ventas")
            print("opcion seleccionada correctamente")
            # Solicita los datos necesarios para registrar una operación de venta y los almacena en el sistema
        elif opcion == "2":
            print("\nCalculo de totales de ingresos")
            print("opcion seleccionada correctamente")
            # Permite calcular el total de ingresos generados por las ventas
        elif opcion == "3":
            print("\nBusqueda de registros")
            print("opcion seleccionada correctamente")
            # Permite buscar informacion de las operaciones de ventas registradas
        elif opcion == "4":
            print("\nLectura de informacion guardada en archivos y reportes")
            print("opcion seleccionada correctamente")
            # Permite consultar la informacion guardada en archivos y reportes generados por el sistema
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            # Finaliza la ejecucion del programa
            break
        else:
            print("\nOpción no valida. Por favor, intente nuevamente.")
