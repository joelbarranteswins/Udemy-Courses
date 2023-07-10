from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QLabel,
    QStatusBar, QToolBar, QDockWidget)
from PySide6.QtGui import QAction, QIcon, Qt
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.construir_menu()
        self.construir_herramientas()
        self.construir_docks()

        self.setCentralWidget(Caja("gray"))

    def construir_docks(self):
        dock = QDockWidget()
        dock.setWindowTitle("DOCK")
        dock.setWidget(Caja("green"))
        # dock.setMinimumHeight(100)
        # dock.setMinimumWidth(120)
        dock.setMinimumSize(120,50)
        dock.setFeatures(QDockWidget.NoDockWidgetFeatures |
                         QDockWidget.DockWidgetFloatable |
                         QDockWidget.DockWidgetClosable | 
                         QDockWidget.DockWidgetMovable)

        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        dock1 = QDockWidget()
        dock1.setWindowTitle("DOCK")
        dock1.setWidget(Caja("purple"))
        # dock.setMinimumHeight(100)
        # dock.setMinimumWidth(120)
        self.addDockWidget(Qt.RightDockWidgetArea, dock1)

        dock2 = QDockWidget()
        dock2.setWindowTitle("DOCK")
        dock2.setWidget(Caja("red"))
        # dock.setMinimumHeight(100)
        # dock.setMinimumWidth(120)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock2)


    def construir_menu(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Menú")
        menu_archivo.addAction("&Prueba")
        submenu_archivo = menu_archivo.addMenu("&Submenú")
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")
        menu_archivo.addSeparator()
        menu_archivo.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")
        menu_ayuda = menu.addMenu("Ay&uda")
        accion_info = QAction("&Información", self)
        accion_info.setIcon(QIcon(absPath("icon.png")))
        accion_info.setShortcut("Ctrl+I")
        accion_info.triggered.connect(self.mostrar_info)
        accion_info.setStatusTip("Muestra información irrelevante")
        menu_ayuda.addAction(accion_info)
        self.setStatusBar(QStatusBar(self))

        # accesores de clase
        self.accion_info = accion_info

    def construir_herramientas(self):
        # Creamos una barra de herramientas
        herramientas = QToolBar("Barra de herramientas principal")
        # Podemos agregar la acción salir implícitamente
        herramientas.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close)
        # O añadir una acción ya creada para reutilizar código
        herramientas.addAction(self.accion_info)
        # La añadimos a la ventana principal
        self.addToolBar(herramientas)

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())