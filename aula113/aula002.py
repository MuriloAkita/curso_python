# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('botão')
botao.setStyleSheet('font-size: 40px; color: red;')

botao2 = QPushButton('botão2')
botao2.setStyleSheet('font-size: 80px; color: blue;')

botao3 = QPushButton('botão3')
botao2.setStyleSheet('font-size: 50px; color: green;')

central_widget = QWidget()

# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout()
central_widget.setLayout(layout)
#                       row, col
layout.addWidget(botao2, 1, 1)
layout.addWidget(botao, 1, 2)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()

app.exec()

