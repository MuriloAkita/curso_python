"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def percentage(num1, num2):
    percentual = num1
    percentual += num1 * (num2/100)
    return percentual


print(percentage(100, 50))
