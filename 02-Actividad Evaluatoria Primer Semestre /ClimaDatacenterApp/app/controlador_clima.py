class ControladorClima:
    def __init__(self, api, historico, alerta):
        self.api = api
        self.historico = historico
        self.alerta = alerta

    def actualizar(self):
        temp = self.api.read_temp()
        hum = self.api.read_humidity()
        self.historico.agregar(temp, hum)
        self.verificar_alertas(temp, hum)

    def verificar_alertas(self, temp, hum):
        if temp > 30:
            self.alerta.enviar_alerta(f"Temperatura crítica: {temp}°C")
        if hum > 80:
            self.alerta.enviar_alerta(f"Humedad crítica: {hum}%")
