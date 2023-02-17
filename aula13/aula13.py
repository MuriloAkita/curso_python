"""
Função len() - contar caracteres
"""

user = input('Digite seu usuário: ')
qtd_char = len(user)

if qtd_char < 6:
    print('Usuário não pode ser menos de 6 caracteres')
else:
    print('Usuário logado')

string1 = input('Digite algo: ')
string2 = input('Digite algo denovo: ')

print(f'A quantidade caracteres digitado foi: {len(string1 + string2)}')
