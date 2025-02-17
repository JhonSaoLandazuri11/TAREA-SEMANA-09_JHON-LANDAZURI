from Producto import Producto
class Inventario:
    def __init__(self):
        self.productos = []

    def anadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("ID ya existente.")
        else:
            self.productos.append(producto)

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        for p in self.productos:
            print(p)


def menu():
    inventario = Inventario()

    while True:
        print("\n********** Menú de Inventario ********** ")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.anadir_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for r in resultados:
                print(r)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
