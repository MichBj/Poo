class Figura:
  """Clase base para representar figuras geométricas."""

  def __init__(self, nombre):
    self.nombre = nombre

  def calcular_area(self):
    raise NotImplementedError("El método calcular_area no está implementado.")

  def __str__(self):
    return f"Figura: {self.nombre}"

class Circulo(Figura):
  """Clase que representa un círculo."""

  def __init__(self, nombre, radio):
    super().__init__(nombre)
    self.radio = radio

  def calcular_area(self):
    return 3.1415 * self.radio ** 2

  def __str__(self):
    return f"{super().__str__()}, Radio: {self.radio:.2f}"

class Rectangulo(Figura):
  """Clase que representa un rectángulo."""

  def __init__(self, nombre, base, altura):
    super().__init__(nombre)
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return self.base * self.altura

  def __str__(self):
    return f"{super().__str__()}, Base: {self.base:.2f}, Altura: {self.altura:.2f}"

# Crear objetos de diferentes figuras
circulo1 = Circulo("Circulo 1", 5)
rectangulo1 = Rectangulo("Rectangulo 1", 10, 7)

# Calcular y mostrar el área de cada figura
print(f"{circulo1}: {circulo1.calcular_area():.2f}")
print(f"{rectangulo1}: {rectangulo1.calcular_area():.2f}")

# Demostrar polimorfismo: tratar objetos de diferentes clases de manera uniforme
figuras = [circulo1, rectangulo1]

for figura in figuras:
  print(figura)
  print(f"Área: {figura.calcular_area():.2f}")
  print()
