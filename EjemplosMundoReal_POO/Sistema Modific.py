class Producto:
    def __init__(self, cd, nombre, cantidad, precio):
        self.cd = cd
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.cd}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    cd, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[int(cd)] = Producto(int(cd), nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Creando uno nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print(f"Error: Permisos insuficientes para leer el archivo {self.archivo}.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(f"{producto.cd},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print(f"Error: Permisos insuficientes para escribir en el archivo {self.archivo}.")

    def agregar_producto(self, producto):
        if producto.cd in self.productos:
            print(f"Error: El producto con código {producto.codigo} ya existe.")
        else:
            self.productos[producto.cd] = producto
            self.guardar_inventario()
            print(f"Producto {producto.nombre} agregado exitosamente.")

    def eliminar_producto(self, cd):
        if cd in self.productos:
            del self.productos[cd]
            print("Producto eliminado.")
        else:
            print("¡Error! Producto no encontrado.")

    def actualizar_producto(self, cd, nuevo_cantidad=None, nuevo_precio=None):
        if cd in self.productos:
            if nuevo_cantidad:
                self.productos[cd].cantidad = nuevo_cantidad
            if nuevo_precio:
                self.productos[cd].precio = nuevo_precio
            print("Producto actualizado.")
        else:
            print("¡Error! Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print("Productos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            print("Inventario:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

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
            cd = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.agregar_producto(Producto(cd, nombre, cantidad, precio))
        elif opcion == '2':
            cd = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(cd)
        elif opcion == '3':
            cd = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_cantidad = int(input("Ingrese la nueva cantidad (deje en blanco si no desea cambiar): "))
            nuevo_precio = float(input("Ingrese el nuevo precio (deje en blanco si no desea cambiar): "))
            inventario.actualizar_producto(cd, nuevo_cantidad, nuevo_precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_todos_los_productos()
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")



