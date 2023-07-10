path = 'Leccion 20 - Manejo de Archivos\prueba.txt'
try:
    archivo = open(path, 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo')
    #ya no se puede serguir trabajando con el archivo que ya fue cerrado
    # archivo.write('nueva info')
    