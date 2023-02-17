nome = 'Murilo Akita'
iterador = iter(nome)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))

    print('Olha o FOR')
    for letra in iterador:
        print(letra)


    print('Olha o OUTRO FOR')
    for letra in iterador:
        print(letra)



except:
    pass
