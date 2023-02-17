variavel = 'valor'

# def func():
#     print(variavel)
#
# def func2():
#     global variavel
#     variavel = 'Outro Valor'
#     print(variavel)

def func():
    outra_variavel = 'valor'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)

