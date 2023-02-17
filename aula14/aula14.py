"""
Validações
Checar Documentação: https://docs.python.org/3/library/stdtypes.html#:~:text=Processing%20Services%20section.-,String%20Methods
"""

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1 + num2)
# else:
#     print('Não foi possível converter os números.')

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)

except ValueError:
    print('Não foi possível converter os números.')
