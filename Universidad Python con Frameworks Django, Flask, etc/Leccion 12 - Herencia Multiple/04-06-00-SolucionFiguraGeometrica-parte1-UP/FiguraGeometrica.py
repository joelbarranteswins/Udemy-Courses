class FiguraGeometrica:
    def __init__(self, ancho, alto):
        #encapsulando los atributos
        self._ancho = ancho
        self._alto = alto

    @property #nos ayuda a llamar nuestro atirbuto desde fuera
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self.alto} ]'