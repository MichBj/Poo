class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = {}

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro añadido: {libro}")

    def eliminar_libro(self, isbn):
        for i, libro in enumerate(self.libros):
            if libro.isbn == isbn:
                del self.libros[i]
                print(f"Libro con ISBN {isbn} eliminado.")
                return
        print(f"No se encontró ningún libro con ISBN {isbn}.")

    def actualizar_libro(self, isbn, nuevo_titulo=None, nuevo_autor=None, nueva_categoria=None):
        for libro in self.libros:
            if libro.isbn == isbn:
                if nuevo_titulo:
                    libro.titulo = nuevo_titulo
                if nuevo_autor:
                    libro.autor = nuevo_autor
                if nueva_categoria:
                    libro.categoria = nueva_categoria
                print(f"Libro con ISBN {isbn} actualizado.")
                return
        print(f"No se encontró ningún libro con ISBN {isbn}.")

    def buscar_libro(self, nombre):
        resultados = []
        for libro in self.libros:
            if nombre.lower() in libro.titulo.lower():
                resultados.append(libro)
        return resultados

    def mostrar_todos_los_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro in self.libros:
                print(libro)

    def registrar_usuario(self, nombre):
        id_usuario = len(self.usuarios) + 1  # Asigna un ID único
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios[id_usuario] = nuevo_usuario
        print(f"Usuario {nombre} registrado con ID {id_usuario}.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in [libro.isbn for libro in self.libros]:
            usuario = self.usuarios[id_usuario]
            for libro in self.libros:
                if libro.isbn == isbn:
                    usuario.prestar_libro(libro)
                    print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
                    return
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    return
        else:
            print("Usuario no encontrado.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Actualizar libro")
        print("4. Buscar libro")
        print("5. Mostrar todos los libros")
        print("6. Registrar usuario")
        print("7. Dar de baja usuario")
        print("8. Prestar libro")
        print("9. Devolver libro")
        print("10. Listar libros prestados")
        print("11. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor: ")
            categoria = input("Ingrese la categoría: ")
            isbn = input("Ingrese el ISBN: ")
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(nuevo_libro)
        elif opcion == '2':
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)
        elif opcion == '3':
            isbn = input("Ingrese el ISBN del libro a actualizar: ")
            nuevo_titulo = input("Nuevo título (deje vacío si no desea cambiar): ")
            nuevo_autor = input("Nuevo autor (deje vacío si no desea cambiar): ")
            nueva_categoria = input("Nueva categoría (deje vacío si no desea cambiar): ")
            biblioteca.actualizar_libro(isbn, nuevo_titulo, nuevo_autor, nueva_categoria)
        elif opcion == '4':
            nombre = input("Ingrese el nombre o parte del nombre del libro a buscar: ")
            resultados = biblioteca.buscar_libro(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros con ese nombre.")
        elif opcion == '5':
            biblioteca.mostrar_todos_los_libros()
        elif opcion == '6':
            nombre = input("Ingrese el nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)
        elif opcion == '7':
            id_usuario = int(input("Ingrese el ID del usuario a dar de baja: "))
            biblioteca.dar_de_baja_usuario(id_usuario)
        elif opcion == '8':
            id_usuario = int(input("Ingrese el ID del usuario: "))
            isbn = input("Ingrese el ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)
        elif opcion == '9':
            id_usuario = int(input("Ingrese el ID del usuario: "))
            isbn = input("Ingrese el ISBN del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)
        elif opcion == '10':
            id_usuario = int(input("Ingrese el ID del usuario: "))
            biblioteca.listar_libros_prestados(id_usuario)
        elif opcion == '11':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu()