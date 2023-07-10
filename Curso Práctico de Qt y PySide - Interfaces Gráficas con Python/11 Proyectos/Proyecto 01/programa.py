import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
# from Interfaz.helpers import absPath
from Interfaz.ui_tabla import Ui_MainWindow
from pathlib import Path

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # cargamos el contenido del fichero
        with open(self.absPath("clientes.json")) as fichero:
            self.datos = json.load(fichero)

        # definimos la configuración de las columnas (claves del json)
        self.columnas = ["nombre", "empleo", "email"]

        # configuramos la tabla a partir de la información recuperada
        self.tabla.setRowCount(len(self.datos)) #muestra el numero de filas
        self.tabla.setColumnCount(len(self.columnas)) #muestra el numero de columnas
        self.tabla.setHorizontalHeaderLabels(self.columnas) #para mostrar el nombre de las columnas

        for i, fila in enumerate(self.datos):
            for j, columna in enumerate(self.columnas):
                item = QTableWidgetItem() 
                # Con Qt.EditRole se establece el tipo de campo automáticamente
                item.setData(Qt.EditRole, fila[columna]) #establecer el dato
                self.tabla.setItem(i, j, item) #introduce los datos en la la tabla por i y j
    
        #personalizar la tabla
        self.tabla.resizeColumnsToContents() #ancho adecuado

        #edita el nombre de la columna
        self.tabla.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
        self.tabla.setHorizontalHeaderItem(1, QTableWidgetItem("Empleo"))
        self.tabla.setHorizontalHeaderItem(2, QTableWidgetItem("Email"))

        #identifica el cambio establecido
        self.tabla.itemChanged.connect(self.celda_modificada)

    def celda_modificada(self, item):
        # recuperamos la fila y la clave de la columna del item seleccionado
        fila, campo = item.row(), self.columnas[item.column()]
        self.datos[fila][campo] = item.data(Qt.EditRole) #recupera el datos cambiado en la interfaz
        # guardamos el fichero con una funcion creada
        self.guardar_json()

    def guardar_json(self):
        with open(self.absPath("contactos.json"), "w") as fichero:
            json.dump(self.datos, fichero)

    # funcion para obtener el path del fichero
    def absPath(self, file):
        return str(Path(__file__).parent.absolute() / file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
