# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()

window.setCentralWidget(central_widget)
window.setWindowTitle('Primeiro Software')

botao = QPushButton('botão')
botao.setStyleSheet('font-size: 40px; color: red;')

botao2 = QPushButton('botão2')
botao2.setStyleSheet('font-size: 80px; color: blue;')

botao3 = QPushButton('botão3')
botao2.setStyleSheet('font-size: 50px; color: green;')


# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout()
central_widget.setLayout(layout)
#                       row, col
layout.addWidget(botao2, 1, 1)
layout.addWidget(botao, 1, 2)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar (barra de baixo da janela)
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

def fecharJanela():
    window.close()

def exibirVersao(status_bar):
    status_bar.showMessage('Versão: 0.0.1')

# menuBar
menu = window.menuBar()

arquivoMenu = menu.addMenu('Arquivo')
fecharAction = arquivoMenu.addAction('Fechar')
fecharAction.triggered.connect(fecharJanela)

testeMenu = menu.addMenu('Teste')
testeAction = testeMenu.addAction('Fechar')
testeAction.triggered.connect(fecharJanela)

ajudaMenu = menu.addMenu('Ajuda')
versaoAction = ajudaMenu.addAction('Versão')
versaoAction.triggered.connect(lambda: exibirVersao(status_bar))

window.show()

app.exec()

