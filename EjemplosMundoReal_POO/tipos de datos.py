# Programa para calcular el Índice de Masa Corporal (IMC)

def calcular_imc(altura, peso):
    """
    Calcula el Índice de Masa Corporal (IMC) a partir de la altura y el peso.

    Parámetros:
        altura (float): Altura del usuario en metros.
        peso (float): Peso del usuario en kilogramos.

    Retorno:
        float: Valor del IMC.
    """
    imc = peso / (altura * altura)
    return imc

def mostrar_resultado(imc):
    """
    Muestra el resultado del IMC en base a la clasificación establecida por la OMS.

    Parámetro:
        imc (float): Valor del IMC.
    """
    if imc < 18.5:
        resultado = "Bajo peso"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidad grado I"
    elif imc < 40:
        resultado = "Obesidad grado II"
    else:
        resultado = "Obesidad grado III"

    print(f"Su IMC es de {imc:.2f} y se encuentra en la categoría: {resultado}")

# Entrada de datos
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Cálculo del IMC
imc = calcular_imc(altura, peso)

# Mostrar resultado
mostrar_resultado(imc)
