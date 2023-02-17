"""
Lambda
"""
lista = [
    ['P1', 13],
    ['P2', 21],
    ['P3', 25],
    ['P4', 33],
    ['P5', 86]
]

def func(item):
    return item[1]

# lista.sort(key=func, reverse=True) #S/ Lambda

print(sorted(lista, key=lambda i: i[1], reverse=True)) #C/ Lambda

print(lista)
