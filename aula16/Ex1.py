"""
Ex1)
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

if num.isnumeric() and int(num) % 2 == 0:
    print('O número é par.')
elif num.isnumeric() and int(num) % 2 != 0:
    print('O número é impar')
else:
    print('O que foi digitado não é um número inteiro')
