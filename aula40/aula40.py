perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2',
        'respostas': {'a': '1', 'b': '2', 'c': '4'},
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 1+1',
        'respostas': {'a': '2', 'b': '3', 'c': '11'},
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 3*2',
        'respostas': {'a': '4', 'b': '6', 'c': '10'},
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 10*10',
        'respostas': {'a': '100', 'b': '1010', 'c': '10'},
        'resposta_certa': 'a',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Resposta correta.')
        respostas_certas += 1
    else:
        print('Resposta errada.')

porcentagem_acerto = respostas_certas / len(perguntas) * 100
print(f'\nResultado do quiz: {respostas_certas}/{len(perguntas)}.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.2f}%.')
