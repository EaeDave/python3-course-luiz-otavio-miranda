"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         01234
#        -54321

lista_nomes = ['David', 'Camila', 'Liz', 'Tommy']  
lista_nomes.append('Bianca')  # Create (C)
print(lista_nomes[0])  # Read (R)
lista_nomes[3] = 'Tom'  # Update (U)
print(lista_nomes)
lista_nomes.pop()  # Delete (D)
print(lista_nomes)

# del vs pop()

# em del, é possível remover o item pelo índice, sem retornar o valor:
del lista_nomes[3]
print(lista_nomes)

# em pop(), é possível fazer o mesmo, porém retorna o valor deletado, podendo armazenar em variáveis

nome_apagado = lista_nomes.pop(2)
print(nome_apagado)
