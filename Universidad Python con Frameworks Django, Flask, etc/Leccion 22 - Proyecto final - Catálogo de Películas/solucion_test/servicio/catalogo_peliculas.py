import simulador_peru
import pandora
import engine_test
import engine_france
import pandas
import pandas as pd
from abc import ABC, abstractmethod


class Formato:
    def __init__(self, nombre):
        self.nombre = nombre


class Genero:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


terror = Genero("Terror", "Peliculas de terror")
drama = Genero("Drama", "Peliculas de drama")
drama_y_terror = Genero("Drama y terror", "Peliculas de drama y terror")

vhs = Formato("VHS")
dvd = Formato("DVD")
netflix = Formato("Netflix")


class Pelicula:
    def __init__(self, nombre: str, genero: Genero, format: Formato):
        self.nombre = nombre
        self.genero = genero
        self.formato = Formato

    def __str__(self):
        return f'Nombre: {self.nombre}'


shrek = Pelicula("Shrek", drama, vhs)


class PeliculaSearchCriteria:
    nombre: str = None
    genero: Genero = None
    formato: Formato = None


""" class Repository(ABC):
    @abstractmethod
    def agregar(self, pelicula: Pelicula):
        pass

    @abstractmethod
    def eliminar(self, pelicula: Pelicula):
        pass

    @abstractmethod
    def buscar(self, search_criteria: PeliculaSearchCriteria):
        pass

    @abstractmethod
    def listar(self):
        print("listar pelicu") """


class ReposityQuery(Protocol):
    def agregar(self, pelicula: Pelicula):
        pass

    def listar(self):
        print("listar pelicu")


class RepositryCommand(Protocol):
    def agregar(self, pelicula: Pelicula):
        pass

    def eliminar(self, pelicula: Pelicula):
        pass


class PeliculaRepositoryMemory:
    peliculas = []

    def agregar(self, pelicula: Pelicula):
        self.peliculas.append(pelicula)

    def eliminar(self, pelicula: Pelicula):
        self.peliculas.remove(pelicula)

    def buscar(self, search_criteria: PeliculaSearchCriteria):
        for pelicula in self.peliculas:
            if search_criteria.nombre and pelicula.nombre != search_criteria.nombre:
                continue
            if search_criteria.genero and pelicula.genero != search_criteria.genero:
                continue
            if search_criteria.formato and pelicula.formato != search_criteria.formato:
                continue
            return pelicula
        return None

    def listar(self):
        for pelicula in self.peliculas:
            print(pelicula)


class CatalogPeliculasClient:
    pelicula_repository: ReposityQuery = PeliculaRepositoryMemory()


class CatalogPeliculaMaster:
    pelicula_repository: Union[ReposityQuery,
                               RepositryCommand] = PeliculaRepositoryMemory()


class GeneroRepositoryFS:
    def buscar(self, search_criteria: PeliculaSearchCriteria):
        for pelicula in self.peliculas:
            if search_criteria.nombre and pelicula.nombre != search_criteria.nombre:
                continue
            if search_criteria.genero and pelicula.genero != search_criteria.genero:
                continue
            if search_criteria.formato and pelicula.formato != search_criteria.formato:
                continue
            return pelicula
        return None

    def listar(self):
        for pelicula in self.peliculas:
            print(pelicula)

# Pelicula DVD


class PeliculaRepositoryCaja:
    def __init__(self, pelicula):
        self.peliculas = []
        print("pelicula respository caja")

    def listar(self):
        print("abrir caja")
        print("buscar película por caratula")
        print("devolver datos")


class PeliculaRepositoryNetflix:
    def listar(self):
        print("abrir Netflix")
        print("buscar película por en buscador")
        print("devolver datos")


class PeliculaReposityCSV:
    def listar(self):
        print("abrir archivo CSV")
        print("buscar película por nombre")
        print("devolver datos")


pelicula_respository_caja = PeliculaRepositoryCaja()
# caja
# abc


# OP 1

def make_dataframe(data) -> pandas.DataFrame:
    return pandas.DataFrame(data)

# OP 2


def make_dataframe(pandas, data) -> DataFrame:
    return pandas.DataFrame(data)


make_dataframe(pandora, data)
make_datagrame(pandas, data)


class SimulationEngine:
    pass


class Simulacion:
    result: dict


def make_simulacion(data: dict) -> Simulacion:
    if data == 1:
        engine_france.executar(data)
        Simulacion(result=engine(data))
    if data == 2:
        engine_test.executar(data)
        Simulacion(result=engine(data))
    if data == 3:
        simulador_peru.executar(data)
        Simulacion(result=engine(data))
    return simulacion


def make_simulacion(engine: SimulationEngine, data: dict) -> Simulacion:
    return Simulacion(result=engine.executar(data))


class ColisionadorAdronesService():
    make_simulacion(engine_france, data)


class TestColisionadorAdrones:
    def test_colisionador_adrones(self):
        simulacion = make_simulacion(engine_test, data)
        colisionador_adrones = ColisionadorAdrones()
        colisionador_adrones.colisionar(simulacion)


class PeliculaGenero:
    genero_name: str


class PeliculaFormato:
    fomato_name: str


class Pelicula(PeliculaGenero, PeliculaFormato, PeliculaDuracion):
    # genero_name
    # formato_name


class PeliculaTerror(Pelicula):
    pass


class RecomendadorPelicula:
    repository: ReposityQuery

    def listar_peliculas(self):
        return self.repository.listar()


class CatalogoPeliculas:
    directory = 'Leccion 22 - Proyecto final - Catálogo de Películas/solucion_test'
    ruta_archivo = 'peliculas.txt'
    path = directory + ruta_archivo

    @classmethod
    def agregar_pelicula(cls, pelicula: Peliculas):
        with open(cls.ruta_archivo, 'a', encoding='utf-8') as File:
            n_pelicula = Peliculas(nombre=pelicula)
            File.write(f'{n_pelicula.nombre}\n')
            print('Se introdujo'.center(50, '-'))
            print(f'se introdujo la pelicula: {n_pelicula.nombre}')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf-8') as File:
            print('Catalogo de peliculas'.center(50, '-'))
            print(File.read())

    @staticmethod
    def eliminar_listas():
        with open(CatalogoPeliculas.ruta_archivo, 'w', encoding='utf-8') as File:
            File.write('')

    @staticmethod
    def opciones_catalogo() -> int:
        intro = int(input('the number please: '))
        if intro == 1:
            pelicula = input('Introduce el nombre de la pelicula: ')
            CatalogoPeliculas.agregar_pelicula(pelicula=pelicula)
        elif intro == 2:
            CatalogoPeliculas.listar_peliculas()
        elif intro == 3:
            CatalogoPeliculas.eliminar_listas()
        elif intro == 4:

            print('Thanks for using this program')
        else:
            print('introduce a number option')
