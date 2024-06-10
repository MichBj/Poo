class Figura:
  """Clase base que representa una figura geométrica."""

  def __init__(self, base, altura):
    """Inicializa la figura con base y altura."""
    self.base = base
    self.altura = altura

  def calcular_area(self):
    """Calcula el área de la figura."""
    raise NotImplementedError("La clase Figura no implementa el método calcular_area()")

class Rectangulo(Figura):
  """Clase que representa un rectángulo."""

  def __init__(self, base, altura):
    """Inicializa el rectángulo con base y altura."""
    super().__init__(base, altura)

  def calcular_area(self):
    """Calcula el área del rectángulo."""
    return self.base * self.altura

class Triangulo(Figura):
  """Clase que representa un triángulo."""

  def __init__(self, base, altura):
    """Inicializa el triángulo con base y altura."""
    super().__init__(base, altura)

  def calcular_area(self):
    """Calcula el área del triángulo."""
    return (self.base * self.altura) / 2

# Crea instancias de las clases Rectangulo y Triangulo
rectangulo = Rectangulo(5, 3)
triangulo = Triangulo(4, 6)

# Calcula y muestra el área de cada figura
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Área del triángulo: {triangulo.calcular_area()}")
