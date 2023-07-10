from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    # Creamos la ventana en el constructor a partir de una QMainWindow
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500,500))
        texto = QLineEdit()
        # capturamos la señal de texto cambiado
        texto.textChanged.connect(self.texto_modificado)

        # establecemos el widget central
        self.setCentralWidget(texto)
        self.texto = texto
        
    def texto_modificado(self):
        texto_recuperado = self.texto.text()
        self.setWindowTitle(texto_recuperado)
        

    # def boton_alternado(self, valor):
    #     if valor:
    #         self.boton.setText('Estoy Activado')
    #     else:
    #         self.boton.setText('Estoy desactivado')
    #     print('boton alternado', valor)

# Si ejecutamos el propio script como programa principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
