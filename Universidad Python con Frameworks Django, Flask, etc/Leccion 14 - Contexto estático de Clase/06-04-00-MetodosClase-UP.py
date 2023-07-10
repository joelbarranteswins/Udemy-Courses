class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    #metodos que se asocian con la clase pero que no pueden estar solas,
    #pero no recibe ningun atributo o variable de la clase
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    #no necesita el parametor self
    #cls es la clase en la que esta ese metodo
    def metodo_clase(cls):
        print(cls.variable_clase)

MiClase.metodo_clase()