import random
import string

# inteiro = random.randint(10, 20) # Gera um número inteiro entre A e B
inteiro = random.randrange(900 , 1000, 10) # Gera um número inteiro entre A e B onde pula de C em C
# flutuante = random.uniform(10, 20) # Gera um numero float entre A e B 

flutuante = random.random() # Gera um numero float aleatorio entre 0 e 1
print(inteiro)
print(flutuante)

lista = ['Luiz,', 'Otavio', 'Maria','Rose', 'João', 'Danilo', 'Felipe']

random.shuffle(lista) # Embaralha a lista

sorteio = random.choice(lista)
# sorteio = random.choices(lista, k=2) # Escolhe 2 valores da lista (pode repetir)
# sorteio = random.sample(lista, k=2) # Escolhe 2 valores da lista (não repetirá)

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%¨&*_'
geral = letras + digitos + caracteres

senha = "".join(random.choices(geral, k=20))

print(senha)
print(sorteio)