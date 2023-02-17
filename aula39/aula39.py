"""
Dicionários
é possivel converter para lista e tupla, vice e versa
"""
import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Murilo', 'Akita']}
d2 = {
    'legal' : 'legal',
    'juntar': 'juntar'
}
v = d1.copy()  # Ele não está copiando, ele está referenciando o d1, então se algo alterar no d1, alterará no v,
# porém se alterar no v, não alterará no d1

# Caso queira fazer uma cópia de verdade do dicionário importar copy
x = copy.deepcopy(d1)

print(x)

v[1] = 'Luiz'
v['d'][0] = 'Juao'
d1.pop(1)
d1.update(d2)

print(d1)
print(v)
print(x)


# clientes = {
#     'cliente1' : {
#         'nome' : 'Murilo',
#         'sobrenome' : 'Akita',
#     },
#     'cliente2': {
#         'nome': 'Dando',
#         'sobrenome': 'Boura',
#     },
#     'cliente3': {
#         'nome': 'Felipe',
#         'sobrenome': 'Beto',
#     }
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo: {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

# d1 = {'nome': 'Murilo',
#       'idade': '21',
#       123: 'teste',
#       (1,2,3,4): 'Tupla'
#       }
#
# # d1['sobrenome'] = 'Akita'
# d1.update({'nova_chave': 'valor'})
#
#
# if 'naoexiste' in d1:
#     print('existe essa chave')
#
# print(d1.get('nome'))
# print(d1)
#
# d2 = dict(nome='Murilo', sobrenome='Akita')
# print(d2)


# d1 = {'str': 'Murilo',
#       123: 'teste',
#       (1, 2, 3, 4): 'Tupla'
#       }
#
# print('str' in d1)
# print('str' in d1.keys())
# print('teste' in d1.values())

# d1 = {'chave1': 'valor',
#       'chave2': 'outro valor',
#       'chave3': 'Murilo',
#       }
#
# for k, v in d1.items():
#     print(k, v)  #chave e valor



