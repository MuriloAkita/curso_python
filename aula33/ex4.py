"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


def fizzbuzz(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        return 'FizzBuzz'
    elif num1 % 3 == 0:
        return 'fizz'
    elif num1 % 5 == 0:
        return 'buzz'
    else:
        return num1


print(fizzbuzz(2))
