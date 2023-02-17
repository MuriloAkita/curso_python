from dados.dados import produtos, pessoas, lista

from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)

print(soma_lista)
print(soma_idades)
print(soma_preco / len(produtos))
print(soma_idades / len(pessoas))


