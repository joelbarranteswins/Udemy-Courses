
class Orden():
    contadorOrdenes = 0
    def __init__(self, producto):
        Orden.contadorOrdenes += 1
        self.Orden_id = Orden.contadorOrdenes
        self._producto = list(producto)
    
    def agregarComputadora(self, new):
        self._producto.append(new)

    def __str__(self):
        if len(self._producto) not in [0, 1]:
            str_producto = ''
            for producto in self._producto:
                str_producto += producto.__str__() + ','
            return f'Orden: {self.Orden_id}\n{str_producto}'
        else:
            return f'Orden: {self.Orden_id}\n{self._producto[0]}'
