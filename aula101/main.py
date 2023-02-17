from zipfile import ZipFile
import os

caminho = 'C:/cursopython/aula101/arquivos/'

with ZipFile('aula101/arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
        
with ZipFile('aula101/arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
        
with ZipFile('aula101/arquivo.zip', 'r') as zip:
    zip.extractall('aula101/descompactado')
