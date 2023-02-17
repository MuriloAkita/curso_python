"""
while em Python - Aula 7
* Utilizado para realizar ações,
* enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

# x = 0  # coluna
# while x < 3:
#     y = 0  # linha
#     while y < 3:
#         print(f'({x},{y})')
#         y += 1
#
#     x += 1
#
# print('Acabou!')

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador(+, -, *, /): ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Digite um número válido.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        print('Não foi possível reconhecer o operador lógico')
        continue

    print(f'{num1} {operador} {num2} = {resultado} \n')


