"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self):
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        return resultado

    def fala_oi(self):
        print('Oi')

    def __setattr__(self, key, value):
        self.__dict__[key] = value


a = A()
b = A()
c = A()

variavel = a(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a.fala_oi()
print(variavel)
a.nome = 'Murilo akita'
print(a.nome)
