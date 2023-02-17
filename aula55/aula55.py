from dados.dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5]

print(nova_lista)
