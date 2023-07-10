class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    #Carcateristicas de Context manager -> enter y exit
    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre: #self.nombre apunta si el archivo esta abierto o no, lo cual devuelve un bool
            self.nombre.close()


#Prueba de retorno de condicional del open
"""print(open('Leccion 21 - Uso de With, Archivos y Resource Manager/prueba.txt'
        ,'w', encoding='utf8'))"""
    
