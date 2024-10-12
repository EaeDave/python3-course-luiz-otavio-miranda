"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('David')

# lista_enumerada = enumerate(lista)  # enumerate é um iterator, retorna um objeto tuple com o index, valor
# print(next(lista_enumerada))  # se faz necessário a chamado do next, que é feito automaticamente com o for

for item in enumerate(lista):
    indice, nome = item  # unpacking
    print(indice, nome)


for indice, nome in enumerate(lista):
    print(indice, nome)


for nome in enumerate(lista):
    print(nome)