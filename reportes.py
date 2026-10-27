
# Modulo de archivos y reportes
# Permite guardar, leer y buscar datos.
# Tambien genera resumenes y estadisticas.

def guardar_datos():
    try:
        archivo = open("datos.txt", "x")
        archivo.write("Sistema de mesa de partes")
        archivo.close()
        print("Datos guardados correctamente.")
    except FileExistsError:
        print("El archivo ya existe. Se conservaron los datos.")


def leer_datos():
    try:
        archivo = open("datos.txt", "r")
        datos = archivo.read()
        archivo.close()
        print(datos)
    except FileNotFoundError:
        print("El archivo datos.txt no existe.")


def buscar_datos():
    buscar = input("Ingrese el dato que desea buscar: ")

    try:
        archivo = open("datos.txt", "r")
        datos = archivo.read()
        archivo.close()

        if buscar.lower() in datos.lower():
            print("Datos encontrados.")
        else:
            print("Datos no encontrados.")

    except FileNotFoundError:
        print("El archivo datos.txt no existe.")


def generar_resumen():
    try:
        archivo = open("datos.txt", "r")
        datos = archivo.read()
        archivo.close()

        print("--- RESUMEN ---")
        print(datos)
        print("Cantidad de palabras:", len(datos.split()))
        print("Cantidad de lineas:", len(datos.splitlines()))
        print("Cantidad de caracteres:", len(datos))

    except FileNotFoundError:
        print("El archivo datos.txt no existe.")


def calcular_estadisticas():
    try:
        archivo = open("datos.txt", "r")
        datos = archivo.read()
        archivo.close()

        print("Cantidad de palabras:", len(datos.split()))
        print("Cantidad de lineas:", len(datos.splitlines()))
        print("Cantidad de caracteres:", len(datos))

    except FileNotFoundError:
        print("El archivo datos.txt no existe.")


def mostrar_estadisticas():
    calcular_estadisticas()


if __name__ == "__main__":
    guardar_datos()
    leer_datos()
    generar_resumen()
    mostrar_estadisticas()

