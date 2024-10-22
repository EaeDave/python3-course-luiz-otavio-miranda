"""
Lista de listas e seu índices
"""

salas = [
    # 0          1
    ['Maria', 'Helena'],  # 0
    # 0
    ['Elaine'],  # 1
    # 0        1        2
    ['Luiz', 'João', 'Eduarda', (0, 1, 2, 3, 4)]  # 2
]

print(salas[2][2])  # 'Eduarda'
print(salas[0][1])  # 'Helena'

print(salas[2][3][0:3])  # (0, 1, 2)

for sala in salas:
    # print(sala)
    for item in sala:
        print(item)