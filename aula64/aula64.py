"""
Criar, ler editar, e deletar arquivos em python
https://docs.python.org/3/library/functions.html#open
"""
import os, json

# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# file.seek(0, 0)
# print('Lendo linhas:')
# print(file.read())
# print('#####################')
#
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline())
# print(file.readline(), end='')
#
# print('#####################')
#
# file.seek(0, 0)
# for linhas in file.readlines():
#     print(linhas, end='')
#
# file.close()

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0, 0)
#     print(file.read())
# except:
#     file.close()

# W reescreve as coisas no arquivo
# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#     file.seek(0, 0)
#     print(file.read())

# A adicionar coisas no arquivo
# with open('abc.txt', 'a+') as file:
#     file.write('Outra Linha\n')
#     file.write('Outra Linha\n')
#     file.write('Outra Linha\n')
#     file.write('Outra Linha\n')
#     file.seek(0, 0)
#     print(file.read())

#Apagando o arquivo:
# os.remove('abc.txt')

# Trabalhando com json

d1 = {
    'Pessoa 1': {
        'nome': 'Murilo',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
    