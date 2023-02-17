"""
Pass e Ellipsis como usar:
"""
valor = True

if valor:
    # Basicamente o pass é utilizado, para que o código não quebre ele "simula" alguma coisa
    # pois o if não pode ser vazio
    pass
    # Caso não use o "pass" é possivel usar o ellipsis (...)
    ...
else:
    print('Tchau!')