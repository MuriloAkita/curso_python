from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays


setlocale(LC_ALL, 'pt_br.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

print(mes_atual, mdays[mes_atual])

