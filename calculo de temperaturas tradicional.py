def ingresar_temperaturas_diarias():
  """
  Esta función permite ingresar las temperaturas diarias de la semana.

  Retorna:
    Una lista con las temperaturas de cada día.
  """
  temperaturas_diarias = []
  for i in range(7):
    temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    temperaturas_diarias.append(temperatura)
  return temperaturas_diarias

def calcular_promedio_semanal(temperaturas):
  """
  Esta función calcula el promedio semanal de las temperaturas.

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
  temperaturas_diarias = ingresar_temperaturas_diarias()
  promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)
  print(f"El promedio semanal de temperaturas es de: {promedio_semanal:.2f} grados Celsius")

if __name__ == "__main__":
  main()
