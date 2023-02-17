"""
Gerador de CPF válido feito em Python
Por Murilo Akita
Github: https://github.com/MuriloAkita
"""

from random import randint


def digit_equation(cpf):
    while len(cpf) != 11:
        summation = 0
        digit = 0
        range_number = len(cpf) + 1

        for i, n in enumerate(range(range_number, 1, -1)):
            summation = summation + (int(cpf[i]) * n)

        remainder = 11 - (summation % 11)

        if remainder <= 9:
            digit = remainder

        cpf += str(digit)
    else:
        return cpf


number = str(randint(100000000, 999999999))
validated_cpf = digit_equation(number)
print(validated_cpf)
