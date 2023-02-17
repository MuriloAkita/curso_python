"""
Inverter valores entre variáveis em Python
"""

x = 10
y = 'Luiz'
z = True

# Normalmente utilizamos assim:
# z = x
# x = y
# y = z

# Em python utilizamos:
x, y, z = z, x, y

print(f'x = {x}\ny = {y}\nz = {z}')
