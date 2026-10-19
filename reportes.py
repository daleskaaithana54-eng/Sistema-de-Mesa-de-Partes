#Modulo de archivos y reportes

# Contar palabras del archivo
def contar_palabras():
    try:
        archivo = open("datos.txt", "r", encoding="utf-8")
        datos = archivo.read()
        archivo.close()

        palabras = datos.split()
        print("Cantidad de palabras:", len(palabras))

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")

# Contar lineas del archivo
def contar_lineas():
    try:
        archivo = open("datos.txt", "r", encoding="utf-8")
        datos = archivo.readlines()
        archivo.close()

        print("Cantidad de lineas:", len(datos))

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")

# Contar caracteres del archivo
def contar_caracteres():
    try:
        archivo = open("datos.txt", "r", encoding="utf-8")
        datos = archivo.read()
        archivo.close()

        print("Cantidad de caracteres:", len(datos))

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")

# Contar cuantas veces aparece una palabra
def contar_busqueda():
    buscar = input("Ingrese la palabra que desea contar: ").strip()

    if buscar == "":
        print("Debe ingresar una palabra.")
        return

    try:
        archivo = open("datos.txt", "r", encoding="utf-8")
        datos = archivo.read()
        archivo.close()

        cantidad = datos.lower().count(buscar.lower())
        print("Veces que aparece la palabra:", cantidad)

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")

# Mostrar resumen completo del archivo
def resumen_completo():
    try:
        archivo = open("datos.txt", "r", encoding="utf-8")
        datos = archivo.read()
        archivo.close()

        palabras = datos.split()
        lineas = datos.splitlines()

        print("\n----- RESUMEN COMPLETO -----")
        print(datos)
        print("Total de palabras:", len(palabras))
        print("Total de lineas:", len(lineas))
        print("Total de caracteres:", len(datos))

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")

# Guardar resumen en un archivo
def guardar_resumen():
    try:
        archivo = open("datos.txt", "r", encoding="utf-8")
        datos = archivo.read()
        archivo.close()

        archivo = open("resumen.txt", "w", encoding="utf-8")
        archivo.write("RESUMEN DEL SISTEMA\n")
        archivo.write(datos)
        archivo.write("\nCantidad de palabras: ")
        archivo.write(str(len(datos.split())))
        archivo.close()

        print("Resumen guardado correctamente en resumen.txt")

    except FileNotFoundError:
        print("Error: no se encontro el archivo datos.txt.")

# Verificar si una palabra existe en el archivo
def verificar_palabra():
    palabra = input("Ingrese la palabra que desea verificar: ").strip()

    if palabra == "":
        print("Debe ingresar una palabra.")
        return

    try:
        archivo = open("datos.txt", "r", encoding="utf-8")
        datos = archivo.read()
        archivo.close()

        if palabra.lower() in datos.lower():
            print("La palabra existe en el archivo.")
        else:
            print("La palabra no existe en el archivo.")

    except FileNotFoundError:
        print("Error: no se encontro el archivo datos.txt.")

# Menu de archivos y reportes
def menu_reportes():
    while True:
        print("\n--- MENU DE REPORTES ---")
        print("1. Contar palabras")
        print("2. Contar lineas")
        print("3. Contar caracteres")
        print("4. Buscar coincidencias")
        print("5. Mostrar resumen completo")
        print("6. Guardar resumen")
        print("7. Verificar palabra")
        print("8. Salir")

        opcion = input("Seleccione una opcion: ")

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
            print("Saliendo del menu de reportes.")
            break
        else:
            print("Opcion no valida.")
