"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('David')

i = 0
for nome in lista:
    print(i, nome)
    i += 1


indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])