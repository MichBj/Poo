class Dibujo:
    """
    Clase que representa un dibujo.

    Atributos:
        figura: Cadena que describe la figura del dibujo.
        color: Cadena que indica el color del dibujo.
    """

    def __init__(self, figura, color):
        """
        Constructor que inicializa los atributos del dibujo.

        Parámetros:
            figura: Cadena que describe la figura del dibujo.
            color: Cadena que indica el color del dibujo.
        """
        self.figura = figura
        self.color = color

        print(f"Creando dibujo: {self.figura} ({self.color})")

    def __del__(self):
        """
        Destructor que se llama cuando el objeto dibujo deja de existir.

        Muestra un mensaje indicando que el dibujo se ha borrado.
        """
        print(f"Borrando dibujo: {self.figura} ({self.color})")


class Borrador:
    """
    Clase que representa una herramienta para borrar un dibujo.

    Atributo:
        dibujo: Objeto de la clase Dibujo que se va a borrar.
    """

    def __init__(self, dibujo):
        """
        Constructor que almacena el dibujo a borrar.

        Parámetros:
            dibujo: Objeto de la clase Dibujo que se va a borrar.
        """
        self.dibujo = dibujo

    def borrar(self):
        """
        Método que borra el dibujo almacenado.

        Invoca al destructor del objeto dibujo para realizar la limpieza.
        """
        del self.dibujo


# Ejemplo de uso
dibujo1 = Dibujo("Círculo", "Rojo")
borrador1 = Borrador(dibujo1)

borrador1.borrar()  # Se borra el dibujo1

# El destructor de dibujo1 se llama automáticamente al salir del bloque

dibujo2 = Dibujo("Cuadrado", "Azul")
borrador2 = Borrador(dibujo2)

del borrador2  # Se elimina el objeto borrador2

# El destructor de dibujo2 se llama automáticamente al eliminar el objeto borrador2
