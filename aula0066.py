"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição
def soma(x, y, z=0):
    print(f'{x=} {y=} | {x} + {y} = {x + y}')


soma(2, 5)
soma(y=5, x=2)  # Argumento nomeado