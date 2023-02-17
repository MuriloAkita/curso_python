"""
Geradores, Iteradores e Iteraveis
"""


################## Iterador #####################
# lista = [0, 1, 2, 3, 4, 5]
# lista = iter(lista)
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# # lista = 12345
# # lista = 'String'
#
# for v in lista:
#     print(v)
# # print(hasattr(lista, '__iter__'))

################## Gerador #####################

import sys
import time


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


# g = gera()
# for v in g:
#     print(v)


def gera2():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


# g2 = gera2()
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))


"""
Anotação:
Os geradores são mais otimizado e menores ao ocupar espaço na memória.
O que faz ele ser assim é que ele só vai criar o valor se caso o código pedir.
"""

