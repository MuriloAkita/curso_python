"""
Validador de CNPJ criado em Python.
Por Murilo Akita
Github: https://github.com/MuriloAkita
"""

from re import findall


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


while True:
    input_cnpj = input("Digite um CNPJ (00.000.000/0000-00): ")
    only_numbers_cnpj = ''.join(findall("\d+", input_cnpj))

    if len(only_numbers_cnpj) != 14:
        print('O CPF deve conter 14 números, digite novamente.')
        continue

    if valida_cnpj(only_numbers_cnpj[:-2]) == only_numbers_cnpj:
        print(f'O CNPJ: {input_cnpj} é VÁLIDO!')
    else:
        print(f'O CNPJ: {input_cnpj} é INVÁLIDO!')
