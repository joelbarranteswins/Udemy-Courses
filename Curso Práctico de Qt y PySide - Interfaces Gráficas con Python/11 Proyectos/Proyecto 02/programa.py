import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
from path import absPath
from Interfaz.ui_tabla import Ui_MainWindow

#Enlazar un modelo  con una table view

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # nos conectamos a la base de datos
        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("clientes.db"))
        if not conexion.open():
            print("No se puede conectar a la base de datos")
            sys.exit(True)

        # creamos el modelo
        modelo = QSqlTableModel()
        modelo.setTable("contactos")
        modelo.select()
        #editar el nombre de las columnas
        modelo.setHeaderData(0, Qt.Horizontal, "Id")
        modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        modelo.setHeaderData(2, Qt.Horizontal, "Empleo")
        modelo.setHeaderData(3, Qt.Horizontal, "Email")

        # configuramos la tabla
        self.tabla.setModel(modelo) #establecer el modelo a visualizar
        self.tabla.resizeColumnsToContents()
        # # escondemos la primera columna
        self.tabla.setColumnHidden(0, True) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

