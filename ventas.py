#Modulo de ventas

ventas=[]

def calcular_subtotal(precio,cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal,porcentaje):
    return subtotal *(porcentaje/100)

    
def calcular_total(subtotal,descuento):
    return subtotal - descuento
    
def registrar_venta():
    print("\nREGISTRAR VENTA")

    codigo=input("Ingrese el codigo del producto:")
    producto=input("Ingrese el nombre delproducto:")
    precio=float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("El precio debe ser mayor a cero")
        precio=float(input("Ingrese el precio del producto: "))
    cantidad=int(input("Ingrese la cantidad: "))
    while cantidad <= 0:
        print("La cantidad debe ser mayor a cero")
        cantidad=int(input("Ingrese la cantidad: "))
    porcentaje= float(input("Ingrese descuento (%): "))
    subtotal=calcular_subtotal(precio,cantidad)
    descuento=aplicar_descuento(subtotal,porcentaje)
    total=calcular_total(subtotal,descuento)

    venta = {
        "codigo": codigo,
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total
    }

    ventas.append(venta)
    
    print("\nVenta registrada correctamente")
    print("Producto:", producto)
    print("Subtotal: S/", round(subtotal, 2))
    print("Descuento: S/", round(descuento, 2))

    print("Total: S/", round(total, 2))

def mostrar_ventas():
    print("\nLista de ventas")

    if len(ventas) == 0:
       print("No hay ventas registradas.")
    else:
        for venta in ventas:
     
            print("\nCodigo:", venta["codigo"])
            print("Producto:", venta["producto"])
            print("Precio: S/", venta["precio"])
            print("Cantidad:", venta["cantidad"])
            print("Subtotal: S/", round (venta["subtotal"], 2))
            print("Descuento: S/", round (venta["descuento"], 2))
            print("Total: S/", round (venta["total"], 2))

def menu_ventas():
        while True:
            print("\nMENU DE VENTAS")
            print("1. Registrar venta")
            print("2. Mostrar ventas")
            print("3. Regresar al menu principal")

            opcion = input("Seleccione una opcion:")

            if opcion == "1":
                registrar_venta()

            elif opcion == "2":
                mostrar_ventas()

            elif opcion == "3":
                break

            else:
                print("Opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    menu_ventas()