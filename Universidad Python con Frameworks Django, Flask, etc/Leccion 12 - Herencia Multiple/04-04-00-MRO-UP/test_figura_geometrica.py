from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')

#MRO - Method Resolution Order -> orden de buqueda que se va a ejecutar
print(Cuadrado.mro())