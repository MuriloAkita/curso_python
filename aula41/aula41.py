"""
Sets (Conjuntos)
add (adicionar), update(atualiza), clear, discard

union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elemento que estão nos dois sets, mas não em ambos)
"""
# s1 = {1, 2, 3, 4, 5}
# # ou
# s2 = set()
# s2.add(1)
# s2.add(2)
# s2.add(3)
# s2.add(4)
# s2.add(5)
# s2.discard(3)
# s2.update('Python')
#
# print(s2, type(s2))

#####################################################

# l1 = [1, 2, 3, 1, 1, 1, 3, 4, 5, 6, 6, 2, 2, 3, 'Murilo', 'Murilo', 'murilo']
# l1 = set(l1)
# print(l1)
# l1 = list(l1)
# print(l1)

#####################################################

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 4, 5, 6}

union = s1 | s2
intersection = s1 & s2
difference = s1 - s2
symmetric_difference = s1 ^ s2

print(f'Union (|): {union}')
print(f'Intersection (&): {intersection}')
print(f'Difference (-): {difference}')
print(f'Symmetric Difference (^): {symmetric_difference}')
