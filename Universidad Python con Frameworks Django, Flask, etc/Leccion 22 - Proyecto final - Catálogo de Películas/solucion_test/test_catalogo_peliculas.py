from servicio import CatalogoPeliculas
# from dominio import Peliculas




if __name__ == '__main__':
    while True:
        print("""
            1. Agregar Peliculas
            2. Listar peliculas
            3. Eliminar archivos de peliculas
            4. salir
            """)
        value =  CatalogoPeliculas.opciones_catalogo()
        
