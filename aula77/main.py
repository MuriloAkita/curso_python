from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1 = Cliente('Murilo', 21)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 22)
a1.falar()
a1.estudar()

p1 = Pessoa('Luiz', 23)
p1.falar()


c2 = ClienteVip('Rose', 24, 'Muriel')
c2.se_apresentar()