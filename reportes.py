#Modulo de archivos y reportes
def guardar_datos():
    archivo = open("datos.txt", "w")
    archivo.write("Sistema de mesa de partes")
    archivo.close()
    print("Datos guardados correctamente en datos.txt")

def leer_datos():
    archivo = open("datos.txt", "r")
    datos = archivo.read()
    archivo.close()
    print(datos)
def buscar_datos():
    buscar = input("Ingrese el dato a buscar: ")
    archivo = open("datos.txt", "r")
    datos = archivo.read()
    archivo.close()
    if buscar in datos:
        print("Datos encontrados.")
    else:
        print("Datos no encontrados.")
def generar_resumen():
    archivo = open("datos.txt", "r")
    datos = archivo.read()
    archivo.close()
    print("RESUMEN")
    print(datos)
def calcular_estadisticas():
    archivo = open("datos.txt", "r")
    datos = archivo.read()
    archivo.close()

    cantidad = len(datos)
    print("Cantidad de caracteres en el archivo:", cantidad)
def mostrar_estadisticas():
    calcular_estadisticas()

if __name__ == "__main__":
    guardar_datos()
    leer_datos()
    buscar_datos()
    generar_resumen()
    mostrar_estadisticas()