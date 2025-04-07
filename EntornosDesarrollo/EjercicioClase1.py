
inventario = []


def agregarProducto():
    nombre = input("Nombre del producto: ")
    try:
        cantidad = float(input("Introduce cantidad"))
        precio = float(input("Introduce precio"))
        if cantidad <= 0 or precio <= 0:
            print("La cantidad y el precio tienen que ser positivos")
    except ValueError:
        print("La cantidad y el precio deben ser numeros")

    producto = {
        "nombre":nombre,
        "cantidad":cantidad,
        "precio":precio
    }

    inventario.append(producto)


def mostrarInventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        for id, producto in enumerate(inventario, start=1):
            print(f"{id} - {producto["nombre"]}")


def buscarProducto():
    buscador = input("Qué producto quieres buscar?")

    for producto in inventario:
        if buscador == producto["nombre"]:
            print(producto)

def calcularValorTotal():
    if not inventario:
        print("El inventario esta vacio")

    total = sum(producto['cantidad'] * producto['precio'] for producto in inventario)
    print(f"El valor total del inventario es {total}")
    

def mostrar_menu():
    print("1.Añadir producto")
    print("2. Mostrar inventario")
    print("3. Calcular el valor total")
    print("4. Buscar producto")
    print("5. Salir")


def main():
    
    terminado = True
    while terminado:
        mostrar_menu()
        respuesta = int(input("Seleccione opcion: "))
        if respuesta == 1:
            agregarProducto()
        elif respuesta == 2:
            mostrarInventario()
        elif respuesta == 3:
            calcularValorTotal()
        elif respuesta == 4:
            buscarProducto()
        elif respuesta == 5:
            print("Saliendo del programa")
            terminado = False
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()