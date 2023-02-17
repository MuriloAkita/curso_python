"""
Formatação de Strings
"""
nome = 'Murilo Akita'
idade = 21
altura = 1.85
peso = 105
e_maior = idade > 18
imc = peso / altura**2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maior de idade?', e_maior)
print('IMC:', imc)

print(nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')
print('{0} tem {1} anos e seu IMC é: {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu IMC é: {im:.2f}'.format(n=nome, i=idade, im=imc))
