
path = 'Leccion 20 - Manejo de Archivos\prueba.txt'
try:
    archivo = open(path,'w')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()

