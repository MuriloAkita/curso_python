"""
ffmpeg -i "ENTRADA" -i "legenda" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 "SAIDA"
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = 'F:/Videos/Base Profile'
caminho_destino = 'F:/Videos/Base Profile/saida'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if 'nao_foi' in arquivo:
            caminho_completo = os.path.join(raiz, arquivo)
            nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

            input_legenda = ''
            map_legenda = ''

            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

            arquivo_saida = f'{caminho_destino}/{nome_arquivo}_NOVO.mp4'

            print(arquivo_saida)

            comando = f'{comando_ffmpeg} -i "{caminho_completo}" {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} "{arquivo_saida}"'

            os.system(comando)
