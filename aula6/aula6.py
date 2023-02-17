"""
Variáveis

Iniciar com letra, pode conter números, separar _, letras minúsculas
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
