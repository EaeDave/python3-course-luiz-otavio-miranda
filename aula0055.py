"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.htm
"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')  # Retorna uma string

print(round(numero_3, 2))  # Retorna um float

numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5
print(numero_6)