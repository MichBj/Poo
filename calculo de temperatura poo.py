class RegistroClima:
  """
  Clase que representa la información diaria del clima.

  Atributos:
    temperatura_dia: La temperatura del día actual.
  """

  def __init__(self, temperatura_dia):
    """
    Constructor de la clase.

    Parámetros:
      temperatura_dia: La temperatura del día actual.
    """
    self.temperatura_dia = temperatura_dia

  def ingresar_temperatura(self):
    """
    Método para ingresar la temperatura del día.
    """
    self.temperatura_dia = float(input("Ingrese la temperatura del día: "))

  def calcular_promedio_semanal(self, temperaturas):
    """
    Método para calcular el promedio semanal de temperaturas.

    Parámetros:
      temperaturas: Lista con las temperaturas de cada día.

    Retorna:
      El promedio semanal de las temperaturas.
    """
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

def main():
  """
  Función principal del programa.
  """
  registro_clima = RegistroClima(0)  # Inicializar con temperatura 0

  temperaturas_diarias = []
  for i in range(7):
    registro_clima.ingresar_temperatura()
    temperaturas_diarias.append(registro_clima.temperatura_dia)

  promedio_semanal = registro_clima.calcular_promedio_semanal(temperaturas_diarias)
  print(f"El promedio semanal de temperaturas es de: {promedio_semanal:.2f} grados Celsius")

if __name__ == "__main__":
  main()
