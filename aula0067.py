"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
"""

def soma(x=0, y=0, z=None):  # Valores padrões
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)

soma()
soma(5, 5)
soma(5, 5, 5)