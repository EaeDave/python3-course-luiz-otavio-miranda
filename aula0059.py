# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, ap, u = lista
print(a, ap, u)  # Maria Eduarda

print(*lista)
print(*string)
print(*tupla)

salas = [
    # 0          1
    ['Maria', 'Helena'],  # 0
    # 0
    ['Elaine'],  # 1
    # 0        1        2
    ['Luiz', 'João', 'Eduarda', (0, 1, 2, 3, 4)]  # 2
]

print(salas)
print(*salas)

for sala in salas:
    print(sala)
    for item in sala:
        print(item, end=' ')