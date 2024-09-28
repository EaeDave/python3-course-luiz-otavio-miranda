"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = 0

while contador <= 10:
    # contador = contador + 1
    contador += 1  # contador + ele mesmo uma vez
    print(contador)


print('Acabou')


contador2 = 11

while contador2 > 0:
    contador2 -= 1
    print(contador2)