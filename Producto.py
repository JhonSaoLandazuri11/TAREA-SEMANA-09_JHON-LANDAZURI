class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    #Devuelve el ID del producto
    def get_id(self):
        return self.id
    
    #Devuelve el nombre del producto.
    def get_nombre(self):
        return self.nombre

    #Devuelve la cantidad disponible del producto.
    def get_cantidad(self):
        return self.cantidad

    #Devuelve el precio del producto.
    def get_precio(self):
        return self.precio

    #Modifica el nombre del producto.
    def set_nombre(self, nombre):
        self.nombre = nombre

    #MModifica la cantidad del producto..
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    #Modifica el precio del producto.
    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


