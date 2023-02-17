from classes import Cliente

cliente1 = Cliente('Murilo', 21)
cliente1.insere_endereco('Votuporanga', 'SP')


cliente2 = Cliente('Maria', 42)
cliente2.insere_endereco('Rio de Janeiro', 'RJ')

cliente3 = Cliente('João', 12)
cliente3.insere_endereco('Salvador', 'BA')

print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1

print()


print(cliente2.nome)
cliente2.lista_enderecos()
print()

print(cliente3.nome)
cliente3.lista_enderecos()
print()
