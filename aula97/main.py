"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilizaçã. Muito utilizado por APIs
"""
from aula97.dados import clientes_dicionario, clientes_json
import json

with open('aula97/clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo)

with open('aula97/clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave, valor)
