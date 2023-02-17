"""
Split, Join, Enumerate em Python
* Split - Dividir uma string
* Join - Juntar uma lista
* Enumerate - Enumerar elementos da lista
"""

# string = "O Brasil é o país do futebol, o Brasil é penta."
#
# lista = string.split(' ')
# string2 = ','.join(lista)
#
# print(string)
# print(lista)
# print(string2)

string = 'O brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)

# lista = [
#     [0, 'Luiz'],
#     [1, 'João'],
#     [2, 'Maria']
# ]
#
# for v1, v2 in lista:
#     print(v1, v2)
