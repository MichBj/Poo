from abc import ABC, abstractmethod

class Figura(ABC):
    """Clase abstracta que representa una figura geométrica."""

    def calcular_area(self) -> float:
        """Método abstracto para calcular el área de la figura."""

    def calcular_perimetro(self) -> float:
        """Método abstracto para calcular el perímetro de la figura."""

class Cuadrado(Figura):
    """Clase que representa un cuadrado."""

    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

# Ejemplo de uso
cuadrado = Cuadrado(9) #variable de valor fijo
print(f"Área del cuadrado: {cuadrado.calcular_area()}")  # Salida:
print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro()}")  # Salida: