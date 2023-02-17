"""
Funções - def em Python (Parte 3) - *args **kwargs
"""

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
print(*lista)  # 1 2 3 4 5 (desempacota a lista toda)


# def func(*args):  # esse "args" é uma tupla, e tuplas não podem ser alterado os valores
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
#     args = list(args)  # conversão de tupla para lista
#     return args
#
# print(type(func(1,2,3,4,5)))

######## ARGS #########
# def func(*args):
#     print(args)
#
# func(*lista, *lista2)

######## KWARGS #########
def func(*args, **kwargs):
    print(args)
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('idade não existe')

func(*lista, *lista2, nome='Murilo', sobrenome='Akita', idade='21')


