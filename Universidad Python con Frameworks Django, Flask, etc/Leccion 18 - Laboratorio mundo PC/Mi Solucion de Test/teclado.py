from dispositivo_entrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    def __init__(self, marca, tipo_entrada):
        DispositivoEntrada.__init__(self, marca, tipo_entrada)
        Teclado.contadorTeclados += 1
        self.teclado_id = Teclado.contadorTeclados
    
    def __str__(self):
        return f'Id = {self.teclado_id}, {DispositivoEntrada.__str__(self)}'
        