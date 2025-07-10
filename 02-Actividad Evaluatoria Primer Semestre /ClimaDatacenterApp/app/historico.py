from datetime import datetime

class Historico:
    def __init__(self):
        self.registro = []

    def agregar(self, temp, hum):
        self.registro.append({
            'timestamp': datetime.now().isoformat(),
            'temp': temp,
            'hum': hum
        })

    def listar(self):
        return self.registro
