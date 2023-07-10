from dispositivo_entrada import DispositivoEntrada
from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden


raton = Raton(marca='HP', tipo_entrada='bluetooth')
teclado = Teclado(marca='Oblivion', tipo_entrada='USB')
monitor = Monitor(marca='LG', tamaño=15)

computadora = Computadora(nombre='Acer', monitor=monitor, teclado=teclado, raton=raton)
computadora_1 = Computadora(nombre='HP', monitor=monitor, teclado=teclado, raton=raton)

productos_1 = [computadora]
productos_2 = [computadora, computadora_1]

orden_1 = Orden(producto=productos_1)
orden_2 = Orden(producto=productos_2)
print(orden_1)
print(orden_2)