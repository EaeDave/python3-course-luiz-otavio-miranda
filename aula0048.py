"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'David'
# nome[0] = 'd'  Aqui geraria um erro, porque str é do tipo imutável, do not support item assignment
nome_antigo = nome  # Aqui está sendo feito uma cópia do valor
print(nome_antigo)
nome = 'Laerze'  # Essa variável teve outra atribuição, mas o dado dela não foi mudado
print(nome)

lista = [1, 2, 3, 4]
lista_2 = lista  # Aqui está sendo apontado um local de referência na memória
lista_2[0] = 50
print(lista)  # A lista foi mudada, porque foi apontado uma referência na memória

print(id(lista))  # Ambos os id serão iguais
print(id(lista_2))  # Mesmo id

print()

print(id(nome))  # Ids diferentes
print(id(nome_antigo))  # Ids diferentes

numeros_1 = [1, 2, 3, 4]
numeros_2 = numeros_1.copy()  # Faz uma cópia simples do valor (retorna o valor)
numeros_2[0] = 100

print(numeros_1)  # Mudando o valor de numeros_2, não afetou essa variável
print(numeros_2)