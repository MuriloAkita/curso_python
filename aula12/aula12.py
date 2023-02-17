"""
Operadores Lógicos
and, or, not, in e not in
"""

a = 2
b = 2
c = 3

# (True E True) = True
print(a == b and b < c)


# (True OU True) = True
# (True OU False) = True
# (False OU False) = False
print(a != b or b > c)

# Inverte o valor da expressão: se der True, ele retornará False
if not c > b:
    print('C é maior do que B.')
else:
    print('B é maior do que C.')

nome = 'Murilo Akita'

# Verifica se algo existe dentro de algo
if 'u' in nome:
    print('Existe a letra U no seu nome')

# Verifica se algo não existe dentro de algo
if 'x' not in nome:
    print('Não existe a letra X no seu nome')

"""
Mini sistema de verificação de senha.
"""
user = 'teste'
password = 'q1w2e3r4'

user_input = input('Digite o nome do usuário: ')
password_input = input('Digite a senha: ')

if user == user_input and password == password_input:
    print('Usuário logado com sucesso.')
else:
    print('Usuário ou senha incorretos.')
