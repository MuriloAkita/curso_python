"""
For in em Python
Iterando strings com for
Função range(start = 0, stop, step=1)
"""

# for n in range(0, 10, 1):
#     print(n)
frase = 'Python é vida!'
print(frase)
nova_frase = ''

user_input = input('Digite a letra que ficará maiúscula: ')
user_input2 = input('Digite a letra que desaparecerá: ')

for letra in frase:
    if letra == user_input2.lower():
        continue

    if letra == user_input.lower():
        nova_frase += letra.upper()
    else:
        nova_frase += letra

print(nova_frase)
