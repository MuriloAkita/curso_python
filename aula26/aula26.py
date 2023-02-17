"""
Desempacotamento de listas em Python
"""

lista = ['Luiz', 'João', 'Maria', 2, 3, 23, 2, 32, 423, 45]
# n1, n2, *outra_lista, ultimo_da_lista = lista
*outra_lista, n1, n2 = lista
print(n1, n2, outra_lista)
