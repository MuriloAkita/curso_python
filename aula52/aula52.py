"""
Combinations, Permutations e Product - Itertools

Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabricio', 'Rose']

for grupo in product(pessoas, repeat=2):
    print(grupo)

for grupo in combinations(pessoas, 2):
    print(grupo)

