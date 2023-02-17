"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min,max
range
"""

# texto = 'Valor'
# l1 = ['A', 'B', 'C']
# l2 = [1, 2, 3]
# l3 = l1 + l2  # ou l1.extend(l2)
#
# # Insere um valor no final de uma lista
# l1.append(l2[1])  # ['A', 'B', 'C', 2]
#
# #Insere um valor em um índice especifico na lista
# l1.insert(1, l2[2])  # ['A', 3, 'B', 'C', 2]
#
# #Se não for passado um valor ele removerá o ultimo item da lista
# l1.pop()  # ['A', 3, 'B', 'C']
#
# # Remove valores específicos de uma lista
# del(l3[::2])  # ['B', 1, 3]
#
# print('Lista 3: ', l3)
# print('Lista 1: ', l1)
#
# # Criando listas mais facilmente
# easyList = list(range(1, 10))
# print('EasyList: ', easyList)

secreto = 'purfume'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if chances < 1:
        print('Você perdeu! Tente novamente')
        break

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Ótimo! A letra "{letra}" contém na palavra secreta')
    else:
        print(f'Tente outra vez!')
        chances -= 1
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns! Quer um biscoito? Tmj!')
        break
    else:
        print(secreto_temporario)