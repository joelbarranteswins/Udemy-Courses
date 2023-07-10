class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    #no usa el parametro self
    #no puede acceder a variables de instancia o atributo
    def metodo_estatico():
        print(MiClase.variable_clase)

MiClase.metodo_estatico()