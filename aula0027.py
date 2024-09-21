"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [inicio:fim:passos] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[5])  # U
print(variavel[4:])  # mundo
print(variavel[0:3])  # Olá
print(len(variavel))  # 9 caracteres retornados
print(variavel[::-1])  # inversão da string