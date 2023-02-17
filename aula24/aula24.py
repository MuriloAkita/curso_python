"""
For / Else em Python
"""

palavras = ['Teste', 'Murilo', 'Aula']

for valor in palavras:
    if valor.lower().startswith('t'):
        break
else:
    print('Não existe uma palavra que começa com J.')