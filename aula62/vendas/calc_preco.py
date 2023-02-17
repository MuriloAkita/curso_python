def aumento(valor, porcentagem):
    r = valor + (valor * (porcentagem/100))
    return round(r, 2)


def reducao(valor, porcentagem):
    r = valor - (valor * (porcentagem/100))
    return round(r, 2)

