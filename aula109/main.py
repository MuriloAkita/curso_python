# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from pathlib import Path

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdf_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_FOCUS = PASTA_ORIGINAIS / 'R20230127.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_FOCUS)

# print(len(reader.pages))


# print(page0.extract_text())
# print(page0.images)



files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

with open(PASTA_NOVA / 'merged.pdf', 'wb') as mergedFile:
    merger.write(mergedFile)

# page0 = reader.pages[0]

# writer = PdfWriter()
"""
SEPARAR PDF POR PAGINAS
for i, page in enumerate(reader.pages):
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
"""

# imagem0 = page0.images[0]
"""
EXTRAIR IMAGEM
with open(PASTA_NOVA / imagem0.name, "wb") as fp:
    fp.write(imagem0.data)
"""

