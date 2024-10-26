"""
Operação ternário (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('Valor' if True else 'Outro valor')  # Operação ternária

digito = 9
novo_digito = 0 if digito > 9 else digito  # Operação ternária

print(digito)
print(novo_digito)