class Monitor:
    contadorMonitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self.monitor_id = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño
    
    @property   
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property   
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño
    
    def __str__(self):
        return f'Id = {self.monitor_id}, marca = {self.marca}, tamaño = {self.tamaño}'