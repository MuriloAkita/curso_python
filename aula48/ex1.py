carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

print(carrinho)

total = sum([float(y) for x, y in carrinho])


#Não fazer dessa forma usa, list compreehentions
# total = []
# for produto in carrinho:
#     total.append(produto[1])
# print(sum(total))
