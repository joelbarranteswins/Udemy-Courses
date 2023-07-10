from PySide6.QtWidgets import ( QColorDialog, QFontDialog, QFileDialog,QMessageBox,
QApplication, QMainWindow, QDialogButtonBox, 
QVBoxLayout,QPushButton, QDialog, QDoubleSpinBox, QSpinBox, 
QLineEdit, QListWidget, QComboBox,QLabel, QCheckBox, QRadioButton)
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import QTranslator, QLibraryInfo
from pathlib import Path
import sys
def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(450,450))
        self.setWindowIcon(QIcon(absPath("icon.png")))

        boton = QPushButton('Moatrar dialogo')
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

        self.boton = boton
    
    def boton_clicado(self):
        confirmado, fuente = QFontDialog.getFont(self)
        if confirmado:
            self.boton.setFont(fuente)

        color = QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f"background-color:{color.name()}")

        # valor, confirmado = QInputDialog.getItem(self, "Titulo", "opciones",["er","sd","44"],
        #                     editable=False)
        # if confirmado:
        #     print(valor)

        # fichero, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ".")
        # print(fichero)


        # dialogo = QMessageBox.warning(self, "Error", "seguro que deseas aplicar?", 
        #                 buttons= QMessageBox.Apply | QMessageBox.Cancel)
        # if dialogo == QMessageBox.Apply:
        #     print("aplicar los cambios")
        # else:
        #     print("no se realizara")
        
        
        
        # dialogo = QMessageBox(self)


        # dialogo.setWindowTitle("Titulo de ejemplo")
        # dialogo.setText("esto es un dialogo de prueba")
        # dialogo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # dialogo.button(QMessageBox.Ok).setText("Aceptar")
        # dialogo.button(QMessageBox.Cancel).setText("Vamonos")

        # dialogo.setIcon(QMessageBox.Question)

        # respuesta = dialogo.exec_()

        # if respuesta == QMessageBox.Ok:
        #     print('Se acepta')
        # else:
        #     print("se rechaza")

        # dialogo.exec_()


        # numero = QDoubleSpinBox()
        # numero.setRange(0,15)
        # numero.setSingleStep(0.5)
        # numero.setPrefix("$")
        # numero.setSuffix("%")

        # numero.setValue(8)
        # print(numero.value())

    #     numero.valueChanged.connect(self.valor_cambiado)
    #     # numero.setMaximum(10)
    #     # numero.setMinimum(2)
    #     self.setCentralWidget(numero)

    # def valor_cambiado(self, numero):
    #     print("Valor cambiado", numero)



    #     texto = QLineEdit()
    #     texto.setMaxLength(10)
    #     texto.setPlaceholderText("Escribe lo que te gusta")
    #     texto.textChanged.connect(self.texto_cambiado)
    #     texto.returnPressed.connect(self.enter_presionado)

    #     self.setCentralWidget(texto)

    # def texto_cambiado(self, texto):
    #     print("Texto cambaido", texto)
    
    # def enter_presionado(self):
    #     texto = self.centralWidget().text()
    #     print("enter presionado, texto:", texto)



    #     lista = QListWidget()
    #     lista.addItems(["Opcion 1", "Opcion 2", "Opcion 3"])
    #     lista.currentItemChanged.connect(self.item_cambiado)

    #     print(lista.currentItem())
    #     self.setCentralWidget(lista)

    # def item_cambiado(self, item):
    #     print("nuevo item", item.text())



    #     desplegable = QComboBox()
    #     desplegable.addItems(["","Opción 1", "Opción 2", "joel"])
    #     desplegable.currentIndexChanged.connect(self.indice_cambiado)
    #     desplegable.currentTextChanged.connect(self.texto_cambiado)
    #     print("indice actual", desplegable.currentIndex())
    #     print("texto actual", desplegable.currentText())
    #     self.setCentralWidget(desplegable)
    
    # def indice_cambiado(self, indice):
    #     print("nuevo indice", indice)
        
    # def texto_cambiado(self, texto):
    #     print("Nuevo texto", texto)



        # radial = QRadioButton("Boton radial")
        # radial.toggled.connect(self.estado_cambiado)
        # radial.setChecked(True)
        # print("Radial activado", radial.isChecked)
        # self.setCentralWidget(radial) 

        # etiqueta = QLabel("soy una etiqueta")
        # fuente = QFont('Comic Sans MS', 24)
        # etiqueta.setFont(fuente)
        # self.setCentralWidget(etiqueta)
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # imagen = QPixmap(abspath("naturaleza.jpg"))
        # etiqueta.setPixmap(imagen)
        # etiqueta.setScaledContents(True)

        # casilla = QCheckBox("Casilla de verificación")
        # casilla.setCheckState(Qt.PartiallyChecked)
        
        # casilla.stateChanged.connect(self.estado_cambiado)

        # casilla.setEnabled(False)
        # print("Activada?", casilla.isChecked())
        # print("Parcial?", casilla.isTristate())

        # self.setCentralWidget(casilla)

    # def estado_cambiado(self, estado):
    #     if estado:
    #         print('Casilla marcada')
    #     else:
    #         print('Casilla desmarcada')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    traductor = QTranslator(app)
    traducciones = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qt_es", traducciones)
    app.installTranslator(traductor)
    print(traducciones)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
