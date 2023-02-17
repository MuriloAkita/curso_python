"""
Formatando valores com modificadores - Aula 17
:s - Texto (strings)
:d - Inteiros (int)
:f - Ponto Flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

nome = 'Murilo quaDROS Akita'
nome_formatado = '{:@>15}'.format(nome)
nome_formatado2 = '{n:!>15}{n:!>15}'.format(n=nome)
nome2 = nome.ljust(60, '#')
valor = 1
valor2 = 213

# print('{:.2f}'.format(divisao))
# print(f'{nome:s}')
print('Minusculo: ', nome.lower())
print('Maiusculo: ', nome.upper())
print('Primeiras Letras Maiusculas: ', nome.title())
print(f'S/ FORMAT: {nome:#^30}')
print(f'LJUST: {nome2}')
print(f'C/ FORMAT: {nome_formatado}')
print(f'COM FORMAT2:{nome_formatado2}')
# print(f'{valor:0>10}')
# print(f'{valor2:0>10.2f}')
# print(f'{valor2:0<10}')
# print(f'{valor2:0^10}')
