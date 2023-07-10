class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

#sirve para crear una varibale no definidad dentro de la clase
#porque python es de tipo dinamica
#se puede acceder a dicha variable desde cualquier varibale que haga instancia de la clase
MiClase.variable_clase2 = 'Valor variable clase 2'

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
print(MiClase.variable_clase2)
print(miClase.variable_clase2)
print(miClase2.variable_clase2)
