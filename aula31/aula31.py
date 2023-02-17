"""
Funções - def em Python (Parte 1)
"""


def funcao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    print(msg, nome)
    return f'{msg}, {nome}'

funcao()
funcao(nome='Zezinho', msg='Hi')
funcao('Olá', 'Murilão')
funcao('Tchau', 'Murilão')
funcao('Olá', 'Maria')
funcao('Tchau', 'Murilão')
funcao('Você não sabe', 'Irineu')

variavel = funcao()