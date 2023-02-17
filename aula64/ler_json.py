import json

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)
    print(d1_json)

for chave, valor in d1_json.items():
    print(chave)
    for chave1, valor1 in valor.items():
        print(chave1, valor1)
