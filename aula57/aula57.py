"""
Try except
"""

try:
    a = []

    print(a)
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError) as erro:
    print('Erro do desenvolvedor')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Código executado com sucesso!')
finally:  #Sempre será executado
    print('Finalmente...')

print('Bora continuar')
