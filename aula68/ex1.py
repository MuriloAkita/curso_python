"""
Faça uma lista de tarefas com as seguintes: opções:
 - Adicionar Tarefa
 - Listar Tarefa
 - Opção de Desfazer (a cada vez que chamarmos, desfaz a última ação)
 - Opção de Refazer (a cada vez que chamarmos, refaz a última ação)
"""
tarefas = []
desfazer_tarefas = []


def adicionar_tarefa(tarefa_adicionada):
    tarefas.append(tarefa_adicionada)
    return True


def desfazer():
    try:
        global tarefas, desfazer_tarefas
        desfazer_tarefas.append(tarefas.pop())
        return True
    except IndexError:
        print("\n" * 130)
        print('Não há nada para desfazer.\n')
        return False


def refazer():
    try:
        global desfazer_tarefas, tarefas
        tarefas.append(desfazer_tarefas.pop())
    except IndexError:
        print("\n" * 130)
        print('Não há nada para refazer.\n')
        return False


while True:
    escolha = input("O que deseja fazer?\n "
                    "[1] Adicionar Tarefa\n "
                    "[2] Listar Tarefas\n "
                    "[3] Desfazer\n "
                    "[4] Refazer\n")

    if escolha == '1':
        tarefa_adicionada = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa_adicionada)
        print("\n" * 130)
        print('Tarefa adicionada com sucesso!\n')
        continue
    elif escolha == '2':
        print("\n" * 130)
        print('Listas de tarefas: ')
        for tarefa in tarefas:
            print(f' - {tarefa}')
        print('\n')
    elif escolha == '3':
        if desfazer():
            print("\n" * 130)
            print('Desfazer executado com sucesso!\n')
        else:
            continue
    elif escolha == '4':
        if refazer():
            print("\n" * 130)
            print('Refazer executado com sucesso!\n')
        else:
            continue
    else:
        print("\n" * 130)
        print("Ação desconhecida.\n")
        continue
