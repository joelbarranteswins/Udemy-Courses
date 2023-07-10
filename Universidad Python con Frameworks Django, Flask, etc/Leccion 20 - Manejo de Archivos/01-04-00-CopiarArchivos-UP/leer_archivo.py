# archivo = open('c:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
archivo = open('Leccion 20 - Manejo de Archivos/01-04-00-CopiarArchivos-UP/prueba.txt', 
                'r', encoding='utf8')
# print(archivo.read())

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
# for linea in archivo:
#     print(linea)

# leer lineas
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[2])

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('Leccion 20 - Manejo de Archivos/01-04-00-CopiarArchivos-UP/copia.txt', 
                'a', encoding='utf8') #tambien se puede usar 'w' 
archivo2.write(archivo.read())

archivo.close()
# archivo2.close()
print('se ha terminado el proceso de leer y copiar archivos')