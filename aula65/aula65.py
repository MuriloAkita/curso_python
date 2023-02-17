"""
Funções decoradoras e decoradores
"""


def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou descorada.')
        funcao(*args, **kwargs)
    return slave


@master
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)


variavel = master(fala_oi)

# variavel()
# fala_oi()
outra_funcao('Sou o murilo.')
