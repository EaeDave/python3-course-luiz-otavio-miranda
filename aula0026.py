"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')  # padding pra esquerda
print(f'{variavel: <10}.')  # padding pra direita
print(f'{variavel: ^10}.')  # padding no centro
print(f'{variavel: ^10}.')  # padding no centro
print(f'{1000.487373786287:.1f}')  # Formatando para apenas uma casa decimal
print(f'O hexadecimal de 150 é {150:08x}')  # Formatando exibindo o hexadecimal