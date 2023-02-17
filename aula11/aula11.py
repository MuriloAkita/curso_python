"""
Operadores Relacionais
== > >= < <= !=
"""

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
saldo = 1072.21

idade_minima = 18
idade_maxima = 70

if idade_minima < idade < idade_maxima:
    print(f'Saldo atual: {saldo}')
    saque = float(input('Quanto deseja sacar? '))
    if saque <= 0:
        print('O mínimo de saque é igual R$ 1,00.')
    elif saque > saldo:
        print(f'O maior valor de saque é: R${saldo}')
    else:
        saldo -= saque
        print('Saque realizado com sucesso!')
        print(f'Seu saldo atual é de: R${saldo}')
else:
    print('Você não tem idade para sacar.')