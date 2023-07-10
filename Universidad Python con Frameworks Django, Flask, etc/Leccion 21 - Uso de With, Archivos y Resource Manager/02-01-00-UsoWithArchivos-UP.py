
#Manejo de contexto with o with statement

with open('Leccion 21 - Uso de With, Archivos y Resource Manager/prueba.txt'
        ,'r', encoding='utf8') as archivo:
    print(archivo.read())


#With usa el __enter__ y el __exit__ como metodos internos

