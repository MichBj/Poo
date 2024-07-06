class Celular:
    """
    Clase base que representa un celular genérico.

    Atributos:
        marca: Marca del celular (str).
        modelo: Modelo del celular (str).
        color: Color del celular (str).

    Métodos:
        llamar(self, numero): Realiza una llamada telefónica (str).
        enviar_mensaje(self, numero, mensaje): Envía un mensaje de texto (str).
    """

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def llamar(self, numero):
        print(f"Llamando al número: {numero} desde el celular {self.marca} {self.modelo}")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a: {numero} con el texto: {mensaje} desde el celular {self.marca} {self.modelo}")


class Smartphone(Celular):
    """
    Clase derivada que representa un smartphone, heredando de la clase base `Celular`.

    Atributos adicionales:
        camara: Megapíxeles de la cámara (int).
        sistema_operativo: Sistema operativo del smartphone (str).

    Métodos sobrescritos:
        llamar(self, numero): Realiza una llamada telefónica con opciones adicionales (videollamada, altavoz).
        enviar_mensaje(self, numero, mensaje): Envía un mensaje de texto con opciones adicionales (emojis, adjunto).
    """

    def __init__(self, marca, modelo, color, camara, sistema_operativo):
        super().__init__(marca, modelo, color)
        self.camara = camara
        self.sistema_operativo = sistema_operativo

    def llamar(self, numero, tipo_llamada="voz"):
        if tipo_llamada == "voz":
            super().llamar(numero)
        elif tipo_llamada == "videollamada":
            print(f"Realizando videollamada al número: {numero} desde el smartphone {self.marca} {self.modelo}")
        else:
            print(f"Tipo de llamada no válido: {tipo_llamada}")

    def enviar_mensaje(self, numero, mensaje, adjunto=None):
        if adjunto is None:
            super().enviar_mensaje(numero, mensaje)
        else:
            print(f"Enviando mensaje a: {numero} con el texto: {mensaje} y adjunto: {adjunto} desde el smartphone {self.marca} {self.modelo}")


# Ejemplo de uso
celular_basico = Celular("Nokia", "1100", "negro")
celular_basico.llamar("123456789")
celular_basico.enviar_mensaje("555555555", "Hola, ¿cómo estás?")

smartphone = Smartphone("Samsung", "Galaxy S22", "azul", 108, "Android")
smartphone.llamar("987654321", tipo_llamada="videollamada")
smartphone.enviar_mensaje("777777777", "Estoy bien, gracias. ¿Y tú?", adjunto=":)")
