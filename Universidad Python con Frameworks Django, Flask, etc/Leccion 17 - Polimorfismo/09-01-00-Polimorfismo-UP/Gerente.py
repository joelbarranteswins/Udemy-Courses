from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}]\
                {super().__str__()}'
        #cuando se llama el class.__str__() del padre se usa self, sin embargo
        #como estamos usando super, ya no es necesario.