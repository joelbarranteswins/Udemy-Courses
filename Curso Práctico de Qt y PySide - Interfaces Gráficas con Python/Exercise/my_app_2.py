from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel)
from PySide6.QtCore import QSize
import sys
import random

class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("subventana")
        etiqueta = QLabel(f"soy una subventana... {random.randint(0,100)}")
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ventana principal")
        self.setFixedSize(QSize(450,450))

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.subventana = Subventana()
        
        boton_mostrar = QPushButton("mostrar subventana")
        boton_mostrar.clicked.connect(self.subventana.show)
        layout.addWidget(boton_mostrar)
        
        boton_ocultar = QPushButton("Ocultar subventana")
        boton_ocultar.clicked.connect(self.subventana.hide)
        
        layout.addWidget(boton_ocultar)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

        