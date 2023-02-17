import os
from utils import formata_tamanho

caminho_procura = input('Digite um caminho:')
termo_procura = input('Digite um termo:')

contador = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        try:
            contador += 1
            caminho_completo = os.path.join(raiz, arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
            tamanho = os.path.getsize(caminho_completo)

            print(40 * '#')
            print(f'\nNome: {nome_arquivo}')
            print(f'Extensão: {ext_arquivo}')
            print(f'Tamanho: {formata_tamanho(tamanho)}\n')
        except PermissionError as e:
            print('Sem permissão para visualizar esse arquivo.')
        except FileNotFoundError as e:
            print('Arquivo não encontrado')
        except Exception as e:
            print(f'Erro desconhecido: {e}')
print(f'Foram encontrados {contador} arquivos.')
