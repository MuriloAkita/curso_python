def formata_tamanho(tamanho):
    bytes_padrao = 1024
    kilo = bytes_padrao
    mega = bytes_padrao ** 2
    giga = bytes_padrao ** 3
    tera = bytes_padrao ** 4
    peta = bytes_padrao ** 5
    texto = 'B'

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'KB'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'MB'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'GB'
    else:
        tamanho /= tera
        texto = 'TB'

    tamanho = round(tamanho, 2)

    return f'{tamanho}{texto}'.replace('.', ',')
