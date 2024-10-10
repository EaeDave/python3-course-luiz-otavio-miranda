"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  # Polimorfismo, nesse caso o operador  + está concatenando as duas listas
print(lista_c)

lista_nomes = ['David', 'Camila', 'Amaro']
lista_sobrenomes = ['Rodrigues', 'Santos', 'Silva']
lista_nomes.extend(lista_sobrenomes)  # Este método não retorna nada, mas muda o valor do objeto
print(lista_nomes)