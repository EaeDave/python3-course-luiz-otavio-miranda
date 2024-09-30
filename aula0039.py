"""
Iterando strings com while
"""
#       012345678910...
nome = 'David Rodrigues'  # Iteráveis
tamanho_nome = len(nome)

x = 0  # Variável de controle do laço
while x < tamanho_nome:
    print(nome[x])
    x += 1

y = 0  # Variável de controle do laço
nova_string = ''
while y < tamanho_nome:
    nova_string += nome[y] + '*'
    y += 1


print(nova_string)