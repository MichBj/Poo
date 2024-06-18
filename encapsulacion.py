class CuentaBancaria:
    """Clase que representa una cuenta bancaria."""

    def __init__(self, titular: str, saldo: float):
        self._titular = titular  # Atributo privado
        self._saldo = saldo

    @property
    def titular(self) -> str:
        """Devuelve el titular de la cuenta."""
        return self._titular

    @titular.setter
    def titular(self, nuevo_titular: str):
        """Establece el titular de la cuenta."""
        if not nuevo_titular:
            raise ValueError("El titular no puede ser vacío")
        self._titular = nuevo_titular

    def depositar(self, monto: float):
        """Deposita un monto en la cuenta."""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo")
        self._saldo += monto

    def retirar(self, monto: float):
        """Retira un monto de la cuenta."""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= monto

# Ejemplo de uso
c=float(1500.7)
cuenta = CuentaBancaria(input("Titular: "),c)
print(f"Titular: {cuenta.titular}")  # Salida: Titular: Juan Pérez
cuenta.titular = input("Nuevo Titular: ")  # Modificación válida
print(f"Titular: {cuenta.titular}")  # Salida: Titular: María Gómez
print(f"Saldo: ",c)
cuenta.depositar(float(input("Monto a depositar: ")))
print(f"Saldo: {cuenta._saldo}")  # Salida: Saldo: 1500
cuenta.retirar(float(input("Monto a retirar: ")))
print(f"Saldo: {cuenta._saldo}")  # Salida: Saldo: 1300

