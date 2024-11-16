
from sys import exit

# Coletando o CPF e validando
CPF = input('Digite seu CPF: ').replace('.', '').replace('-', '')
if CPF.__len__() > 11:
    print(f'CPF {CPF} inválido, deve ter no máximo 11 caracteres.')
    exit()
if CPF.__len__() < 9:
    print('O CPF deve conter pelo menos os 9 primeiros dígitos.')
    exit()
try:
    validar_se_cpf_so_possui_numeros = int(CPF)
except ValueError:
    print('Digite somente números.')
    exit()
# Obtendo a soma
contador = 10
soma = 0
for index, numero in enumerate(CPF):
    valor = int(numero) * contador
    contador -= 1
    soma += valor
    if index == 8:
        break

# Obtendo o resultado do primeiro dígito
primeira_etapa = soma * 10
segunda_etapa = primeira_etapa % 11
primeiro_digito = 0 if segunda_etapa > 9 else segunda_etapa

print(f'O primeiro dígito do CPF é = {primeiro_digito}')

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


segundo_digito = soma + primeiro_digito




