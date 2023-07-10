class Peliculas:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def __str__(self):
        return f'Nombre: {self.nombre}'


if __name__ == '__main__':
    a = Peliculas(nombre='batman')
    print(a.nombre)

