from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Hugo', 'nota': 'B'},
    {'nome': 'Vitor', 'nota': 'C'},
    {'nome': 'Leticia', 'nota': 'A'},
    {'nome': 'Murilo', 'nota': 'C'},
    {'nome': 'Isabela', 'nota': 'D'},
    {'nome': 'Maria', 'nota': 'F'},
    {'nome': 'João', 'nota': 'E'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_grouped = groupby(alunos, ordena)


#Nota: Antes de usar o groupby é preciso ordenar os valroes
for nota, alunos in alunos_grouped:
    va1, va2 = tee(alunos)

    print(f'Nota: {nota}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\tQuantidade de alunos que tiraram nota {nota}: {quantidade}')
    print()


