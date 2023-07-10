class Computadora:
    contadorComputadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.Computadora_id = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    
    @property   
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    def __str__(self):
        return f'computadoras: \n     {self._nombre}: {self.Computadora_id}\n\
            Monitor: {self._monitor.__str__()}\n\
            Teclado: {self._teclado.__str__()}\n\
            Raton: {self._raton.__str__()}'