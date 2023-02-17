"""
Manipulando strings - Aula 18
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
* https://docs.python.org/3/library/stdtypes.html (tipos built-in)
* https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos   [012345678]
texto       = 'Python <3'
# negativos  -[987654321]
print(texto[8])
print(texto[-9])

nova_string = texto[0:6]  # [:6] ou [7:]
nova_string_passo = texto[0:6:2]  # Nesse caso o 2 é de quantas em quantas casas ele pula
print(nova_string)
print(nova_string_passo)

for letra in texto:
    print(letra)

