from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QLineEdit, QSpinBox, QPushButton, QPlainTextEdit, QVBoxLayout, QCheckBox, QRadioButton)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        formulario = QFormLayout() 
        formulario.addRow("QCheckBox", QCheckBox())
        formulario.addRow("QRadioButton", QRadioButton())

        

        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))
        formulario.addRow("QSpinBox", QSpinBox())

        etiqueta = QLabel("QLabel")
        etiqueta.setObjectName("etiqueta")
        formulario.addRow(etiqueta)

        

        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)

        self.setStyleSheet(""" 
            QMainWindow {background-color: #212121} 
            QLabel {color: #e9e9e9}
            QPushButton {
                background-color: orange;
                font-family: "Arial";
                font-size: 14px;
                font-weight: bold;}
            #etiqueta {background.color: cyan; padding: 10px; color: black;}
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())