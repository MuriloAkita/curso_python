"""
Desafio Aula 8
* Criar variáveis para nome (str), idade (int)
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valroes na tela usando F-Strings (com chaves)
"""

import datetime

nome = 'Murilo Akita'
idade = 21
altura = 1.85
peso = 105
imc = peso / altura**2

year = datetime.date.today().year
birth_year = year - idade

print(f'{nome} tem {idade} anos, tem {altura}m, pesa {peso}kgs, nasceu em {birth_year}, e seu IMC é:{imc:.2f}')
