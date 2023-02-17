"""
Operador ternário em python
"""

# logged_user = False
# msg = 'Usuário Logado.' if logged_user else 'Usuário precisa logar.'
#
# print(msg)

idade = input('Qual sua idade? ')

if not idade.isnumeric():
    print('Digite um número.')
else:
    maioridade = (int(idade) >= 18)
    msg = 'Pode acessar' if maioridade else 'Não pode acessar.'

    print(msg)
