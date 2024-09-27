"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = int(input('Digite um número inteiro: '))
e_par = numero % 2 == 0

if e_par:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} não é par.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual = float(input('Digite a hora atual: '))

if hora_atual >= 0 and hora_atual <= 11:
    print('Bom dia :)')
elif hora_atual > 11 and hora_atual <= 17:
    print('Boa tarde :)')
elif hora_atual > 17 and hora_atual <= 23.59:
    print('Boa noite!')
else:
    print('Hora inválida.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if nome.__len__()  <= 4:
    print('Seu nome é curto')
elif nome.__len__()  > 4 and nome.__len__() < 7:
    print('Seu nome é médio')
elif nome.__len__() > 6:
    print('Seu nome é muito grande')