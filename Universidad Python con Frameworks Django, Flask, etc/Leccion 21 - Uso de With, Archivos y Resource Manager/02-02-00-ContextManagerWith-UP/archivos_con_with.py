from ManejoArchivos import ManejoArchivos

# with open('prueba.txt','r', encoding='utf8') as archivo:
directory = 'Leccion 21 - Uso de With, Archivos y Resource Manager/02-02-00-ContextManagerWith-UP'
archivo = '/prueba.txt'
path = directory + archivo
with ManejoArchivos(path) as archivo:
    print(archivo.read())



