"""
Ex2)
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hour = input('Que horas são? ')
print(hour)

if hour.isnumeric() and (0 <= int(hour) <= 11):
    print('Bom dia!')
elif hour.isnumeric() and (12 <= int(hour) <= 17):
    print('Boa tarde!')
elif hour.isnumeric() and (18 <= int(hour) <= 23):
    print('Boa Noite!')
elif hour.isnumeric() and int(hour) > 23:
    print('Número é maior que 23')
else:
    print('Insira um número inteiro até 23')