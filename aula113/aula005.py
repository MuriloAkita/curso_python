# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (button)
#               -> Widget 2 (button2)
#               -> Widget 3 (button3)
#   -> show
# -> exec

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Primeiro Software')
        
        # Botão1
        self.button1 = self.make_button('Botão 1')
        self.button1.clicked.connect(self.slotOnCheck)

        # Botão2
        self.button2 = self.make_button('Botão 2')
        
        # Botão3
        self.button3 = self.make_button('Botão 3')

        # layout = QVBoxLayout()
        # layout = QHBoxLayout()
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        #                       row, col
        self.grid_layout.addWidget(self.button1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        # statusBar (barra de baixo da janela)
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()

        self.fileMenu = self.menu.addMenu('Arquivo')
        self.closeAction = self.fileMenu.addAction('Fechar')
        self.closeAction.triggered.connect(self.slotCloseWindow)

        self.checkBoxAction = self.fileMenu.addAction('teste')
        self.checkBoxAction.setCheckable(True)
        self.checkBoxAction.toggled.connect(self.slotOnCheck)  # Quando marcar...
        self.checkBoxAction.hovered.connect(self.slotOnCheck) # Quando passar o mouse em cima...

        self.helpMenu = self.menu.addMenu('Ajuda')
        self.versionAction = self.helpMenu.addAction('Versão')
        self.versionAction.triggered.connect(self.slotViewVersion)

    @Slot()
    def slotCloseWindow(self):
        self.close()

    @Slot()
    def slotViewVersion(self):
        self.status_bar.showMessage('Versão: 0.0.1')

    @Slot()
    def slotOnCheck(self):
        print('Está marcado ?', self.checkBoxAction.isChecked())
        
    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 40px; color: red; background-color: blue;')
        return btn


app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec()
