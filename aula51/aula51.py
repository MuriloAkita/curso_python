"""
count = Itertools
"""
from itertools import count

contador = count(start=-1, step=-1)

for valor in contador:
    print(round(valor, 2))

    if valor <= 0 or valor >= 10:
        break
