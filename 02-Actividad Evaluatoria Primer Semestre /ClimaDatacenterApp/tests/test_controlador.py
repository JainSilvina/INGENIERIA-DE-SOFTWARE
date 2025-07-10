from app.controlador_clima import ControladorClima
from app.ms_forecast_mock import MSForecastMock
from app.historico import Historico

class MockAlerta:
    def __init__(self):
        self.mensajes = []

    def enviar_alerta(self, mensaje):
        self.mensajes.append(mensaje)

def test_alerta_temperatura():
    api = MSForecastMock()
    api.temperature = 35
    hist = Historico()
    alerta = MockAlerta()
    c = ControladorClima(api, hist, alerta)

    c.actualizar()

    assert "Temperatura crítica" in alerta.mensajes[0]
    assert len(hist.listar()) == 1
