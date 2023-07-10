class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre  
        #para que no se pueda acceder desde afuera se usa self.__nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1._nombre = 'Juan Carlos'
persona1.mostrar_detalle()
