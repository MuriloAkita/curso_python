"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

def funcao1():
    return 'Teste!!'

def funcao2(funcao):
    return funcao1()

print(funcao2(funcao1()))
