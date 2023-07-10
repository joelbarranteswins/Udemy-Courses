# archivo = open('c:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
archivo = open('Leccion 20 - Manejo de Archivos/01-03-00-LeerArchivos-UP/prueba.txt',
                 'r', encoding='utf8')

#lee todos los caracteres
# print(archivo.read()) 

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas y en cada llamado avanza a la siguiente linea
print(archivo.readline()) 
print(archivo.readline())
