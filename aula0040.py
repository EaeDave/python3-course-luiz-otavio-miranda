""" Calculadora com while """

while True:
    escolha = input('Escolha entre somar (+), subtrair (-), multiplicar (*), dividir (/) ou sair (s): ')
    
    somar = escolha.startswith('+')
    subtrair = escolha.startswith('-')
    multiplicar = escolha.startswith('*')
    dividir = escolha.startswith('/')
    sair = escolha.startswith('s')
    
    if somar:
        try:
            valor1 = float(input('Digite o 1° valor da soma: '))
            valor2 = float(input('Digite o 2° valor da soma: '))
            soma = valor1 + valor2
            print(f'{valor1} + {valor2} = {soma}')
        except:
            print('Digite somente números!')
            
    elif subtrair:
        try:
            valor1 = float(input('Digite o 1° valor da subtração: '))
            valor2 = float(input('Digite o 2° valor da subtração: '))
            subtracao = valor1 - valor2
            print(f'{valor1} - {valor2} = {subtracao}')
        except:
            print('Digite somente números!')
    elif multiplicar:
        try:
            valor1 = float(input('Digite o 1° valor da multiplicação: '))
            valor2 = float(input('Digite o 2° valor da multiplicação: '))
            multiplicacao = valor1 * valor2
            print(f'{valor1} * {valor2} = {multiplicacao}')
        except:
            print('Digite somente números!')
    elif dividir:
        try:
            valor1 = float(input('Digite o 1° valor da divisão: '))
            valor2 = float(input('Digite o 2° valor da divisão: '))
            divisao = valor1 / valor2
            print(f'{valor1} / {valor2} = {divisao}')
        except:
            print('Digite somente números!')
    elif sair:
        break
    else:
        print('Operador inválido.')