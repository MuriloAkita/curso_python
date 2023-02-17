import re


def extract_numbers(string):
    numbers_list = re.findall("\d+", string)
    numbers = ''

    for n in numbers_list:
        numbers += n
    return numbers


def digit_equation(cpf):
    formatted_cpf = cpf[:-2]
    while len(formatted_cpf) != 11:
        summation = 0
        digit = 0
        range_number = len(formatted_cpf) + 1

        for i, n in enumerate(range(range_number, 1, -1)):
            summation = summation + (int(formatted_cpf[i]) * n)

        remainder = 11 - (summation % 11)

        if remainder <= 9:
            digit = remainder

        formatted_cpf += str(digit)
    else:
        return formatted_cpf


while True:
    input_cpf = input('Digite seu CPF: ')

    cpf_numbers = extract_numbers(input_cpf)

    if len(cpf_numbers) != 11:
        print('O CPF deve conter 11 números, digite novamente.')
        continue

    new_cpf = digit_equation(cpf_numbers)

    if new_cpf != cpf_numbers:
        print('Este CPF é inválido')
        break

    print('CPF Válido!')
    break
