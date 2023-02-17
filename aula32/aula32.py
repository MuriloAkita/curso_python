"""
Funções - def em Python (Parte 2)
"""

# def funcao(var):
#     print(var)
#
# variavel = funcao('Olá Mundo!')
# print(variavel)  # Irá retornar None pois não dei nenhum return na função

def dumb():
    return ('Murilo', 'Akita')

var = dumb()
print(var[1], type(var))