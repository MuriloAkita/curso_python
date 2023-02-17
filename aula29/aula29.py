"""
Operador Or para if e else em python
"""

nome = input('Qual o seu nome? ')

# Normalmente fazemos assim.
# if nome:
#     print(nome)
# else:
#     print('Você não digitou nada =(')

# Porém podemos fazer dessa forma:
print(nome or 'Você não digitou nada!')

# Ele só vai parar na primeira expressão verdadeira que no caso é a string
# print(nome or None or False or 0 or 'Você não digitou nada!')

# Exemplo abaixo:

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Eba!'

variavel = a or b or c or d or e or f or g

print(variavel)