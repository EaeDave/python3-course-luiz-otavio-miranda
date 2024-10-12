"""
Introdução ao desempacotamento + tuples (tuplas)
"""

nomes = ['Maria', 'Helena', 'Luiz', 'David']

nome1, nome2, nome3, nome4 = nomes  # Desempacotamento

nome_inicial, *nomes_desconhecidos, nome_final = nomes  # Desempacotamento sem saber a qtd de

print(nome2)

print(nomes_desconhecidos)  # nomes_desconhecidos é o retorno do restantes dos valores da lista original, em lista
print(*nomes_desconhecidos)  # Colocando o sinal de *, é feito o unpack da lista, assim, exibindo as strings sequenciais

numeros = [1, 2, 3, 4, 5]

_, _, numero3, *_ = numeros  # O _ é utilizado por convesão para informar que a variável é irrelevante, talvez não será usada

print(numero3)