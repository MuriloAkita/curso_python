"""
# Iteração While com strings
"""

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
print(tamanho_frase)

contador = 0
nova_string = ''

input_do_user = input('Qual letra deseja colocar maiúscula? ')

while contador < tamanho_frase:
    print(frase[contador], contador)

    if frase[contador] == input_do_user.lower():
        nova_string += frase[contador].upper()
    else:
        nova_string += frase[contador]

    contador += 1

print(nova_string)

