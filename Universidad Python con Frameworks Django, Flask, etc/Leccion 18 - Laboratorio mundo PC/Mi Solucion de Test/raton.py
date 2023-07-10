from dispositivo_entrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contadorRatones = 0
    def __init__(self, marca, tipo_entrada):
        DispositivoEntrada.__init__(self, marca, tipo_entrada)
        Raton.contadorRatones += 1
        self.raton_id = Raton.contadorRatones
    
    def __str__(self):
        return f'Id = {self.raton_id}, {DispositivoEntrada.__str__(self)}'