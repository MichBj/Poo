class Producto:
    # Representa un producto con sus atributos: ID, nombre, cantidad y precio
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id  # Identificador único del producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Representación en cadena del objeto Producto para facilitar la impresión
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los productos
        self.productos = []

    def agregar_producto(self, producto):
        # Verifica si ya existe un producto con el mismo ID
        if any(p.id == producto.id for p in self.productos):
            print("¡Error! Ya existe un producto con ese ID.")
            return  # Sale de la función si se encuentra un duplicado
        self.productos.append(producto)  # Agrega el producto a la lista

    def eliminar_producto(self, id):
        # Busca el producto por su ID y lo elimina de la lista
        for i, producto in enumerate(self.productos):
            if producto.id == id:
                del self.productos[i]
                print("Producto eliminado.")
                return
        print("¡Error! Producto no encontrado.")

    def actualizar_producto(self, id, nuevo_cantidad=None, nuevo_precio=None):
        # Busca el producto por su ID y actualiza los atributos especificados
        for producto in self.productos:
            if producto.id == id:
                if nuevo_cantidad:
                    producto.cantidad = nuevo_cantidad
                if nuevo_precio:
                    producto.precio = nuevo_precio
                print("Producto actualizado.")
                return
        print("¡Error! Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos cuyo nombre coincida (insensible a mayúsculas y minúsculas)
        resultados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print("Productos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        # Muestra todos los productos del inventario
        if self.productos:
            print("Inventario:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

# Interfaz de usuario simple para interactuar con el inventario
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == '2':
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_cantidad = int(input("Ingrese la nueva cantidad (deje en blanco si no desea cambiar): "))
            nuevo_precio = float(input("Ingrese el nuevo precio (deje en blanco si no desea cambiar): "))
            inventario.actualizar_producto(id, nuevo_cantidad, nuevo_precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_todos_los_productos()
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")