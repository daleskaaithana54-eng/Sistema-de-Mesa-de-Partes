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
            # Lógica para gestionar ventas
        elif opcion == "2":
            print("\nCalculo de totales de ingresos")
            # Lógica para gestionar ingresos
        elif opcion == "3":
            print("\nBusqueda de registros")
            # Lógica para gestionar gastos
        elif opcion == "4":
            print("\nLectura de informacion guardada en archivos y reportes")
            # Lógica para gestionar archivos y reportes
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            # Lógica para mostrar resumen general
            break
        else:
            print("\nOpción no valida. Por favor, intente nuevamente.")
