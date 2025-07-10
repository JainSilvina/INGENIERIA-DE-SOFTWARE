from flask import Flask, request
from app.controlador_clima import ControladorClima
from app.historico import Historico
from app.alerta_email import AlertaEmail
from app.ms_forecast_mock import MSForecastMock

app = Flask(__name__)
api = MSForecastMock()
hist = Historico()
alerta = AlertaEmail()
controlador = ControladorClima(api, hist, alerta)

@app.route("/update", methods=["POST"])
def update():
    controlador.actualizar()
    return {"status": "ok", "historial": hist.listar()}

if __name__ == "__main__":
    app.run(port=5000)
