class Persona:
    def __init__(self, nombre, edad):
        # __init__ inizializa el metodo
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        # Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo

empleado1 = Empleado('Juan', 28, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
