"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
try:
    int('a')  # Não é possível converter string para int.
except:
    print('Ocorreu um erro!')  # Essa mensagem que será exibida.

try:
    numero = int(input('Vou dobrar o número que você digitar: '))
    print(f'O dobro de {numero} é {numero * 2}')
except:
    print('Você digitou um caractere inválido, digite somente números.')