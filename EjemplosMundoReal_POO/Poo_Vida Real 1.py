class Lapiz:
    """
    Clase que representa un lápiz.
    """

    def __init__(self, marca, color, mina, borrador):
        """
        Constructor de la clase Lápiz.

        Parámetros:
            marca (str): Marca del lápiz.
            color (str): Color del lápiz.
            mina (str): Tipo de mina del lápiz (HB, 2H, etc.).
            borrador (bool): Indica si el lápiz tiene borrador.
        """
        self.marca = marca
        self.color = color
        self.mina = mina
        self.borrador = borrador

    def escribir(self, texto):
        """
        Método que simula el uso del lápiz para escribir.

        Parámetro:
            texto (str): Texto a escribir.
        """
        print(f"Escribiendo con el lápiz {self.marca} {self.color} ({self.mina}): {texto}")

    def borrar(self, texto):
        """
        Método que simula el uso del borrador del lápiz (si lo tiene).

        Parámetro:
            texto (str): Texto a borrar.
        """
        if self.borrador:
            print(f"Borrando con el borrador del lápiz {self.marca} {self.color}: {texto}")
        else:
            print(f"El lápiz {self.marca} {self.color} no tiene borrador.")


#2. Clase Licuadora:**


class Licuadora:
    """
    Clase que representa una licuadora.
    """

    def __init__(self, marca, modelo, potencia, capacidad):
        """
        Constructor de la clase Licuadora.

        Parámetros:
            marca (str): Marca de la licuadora.
            modelo (str): Modelo de la licuadora.
            potencia (int): Potencia de la licuadora en watts.
            capacidad (float): Capacidad de la licuadora en litros.
        """
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.capacidad = capacidad

    def licuar(self, ingredientes):
        """
        Método que simula el uso de la licuadora para preparar un licuado.

        Parámetro:
            ingredientes (str): Lista de ingredientes a licuar.
        """
        print(f"Licuando con la licuadora {self.marca} {self.modelo} ({self.potencia}W, {self.capacidad}L): {ingredientes}")


#**Ejemplo de uso:**

# Crear objetos Lápiz y Licuadora
lapiz1 = Lapiz("Faber-Castell", "Amarillo", "HB", True)
licuadora1 = Licuadora("Oster", "BLSTGM2000", 600, 1.5)

# Usar métodos de los objetos
lapiz1.escribir("Hola, mundo!")
lapiz1.borrar("Mundo")
licuadora1.licuar("Frutas, leche, yogurt")

# Interacción entre objetos
lapiz1.escribir("Ingredientes para licuado:")
licuadora1.licuar(lapiz1.escribir("Frutas, leche, yogurt"))
