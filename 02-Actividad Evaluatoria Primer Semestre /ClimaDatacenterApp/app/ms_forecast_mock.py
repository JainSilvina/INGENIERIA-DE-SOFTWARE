class MSForecastMock:
    def __init__(self):
        self.temperature = 25
        self.humidity = 50

    def up_temp(self, x):
        self.temperature += x

    def down_temp(self, x):
        self.temperature -= x

    def up_humidity(self, x):
        self.humidity += x

    def down_humidity(self, x):
        self.humidity -= x

    def read_temp(self):
        return self.temperature

    def read_humidity(self):
        return self.humidity
