"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'David'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)  # Aqui aconteceu a interpolação de string
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))