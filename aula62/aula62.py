import vendas.calc_preco

preco = 49.90
preco_com_aumento = vendas.calc_preco.aumento(valor=preco, porcentagem=15)

print(preco_com_aumento)
