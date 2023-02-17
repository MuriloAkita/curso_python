"""
Gerador de CNPJ criado em Python.
Por Murilo Akita
Github: https://github.com/MuriloAkita
"""

from re import findall
from random import randint


def valida_cnpj(cnpj):
    multiplicador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    novo_cnpj = cnpj
    while len(novo_cnpj) != 14:
        summation = 0
        for x, y in enumerate(multiplicador):
            summation += int(novo_cnpj[x]) * y
        if (11 - (summation % 11)) > 9:
            novo_cnpj += str(0)
        else:
            digit = 11 - (summation % 11)
            novo_cnpj += str(digit)

        multiplicador.insert(0, 6)
    else:
        return novo_cnpj


cnpj = number = str(randint(10000000, 99999999)) + '0001'
only_numbers_cnpj = ''.join(findall("\d+", cnpj))

print(valida_cnpj(cnpj))
