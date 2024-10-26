"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

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
resultado = 0 if segunda_etapa > 9 else segunda_etapa

print(f'O primeiro dígito do CPF é = {resultado}')

    




