"""
Tuplas
"""
tupla1 = (1, 2, 3, 'a', 'Murilo Akita')
tupla2 = (4, 5, 6, 'a', 'Murilo Akita')

tupla = tupla1 + tupla2

lista_tupla = list(tupla)
lista_tupla[1] = 1000
tupla_lista = tuple(lista_tupla)
print(lista_tupla)
print(tupla_lista)


# for v in tupla1:
#     print(v)

