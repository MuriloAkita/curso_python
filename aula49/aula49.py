"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Votuporanga']
estados = ['SP', 'MG', 'BA']

cidades_estados1 = zip(indice, cidades, estados)
# cidades_estados2 = zip_longest(
#     indice,
#     cidades,
#     estados,
#     fillvalue='SP')

# print(list(cidades_estados1))
# print(list(cidades_estados2))

for indice, cidade, estado in cidades_estados1:
    print(indice, cidade, estado)
