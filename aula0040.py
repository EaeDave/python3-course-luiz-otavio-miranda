""" Calculadora com while """
calcular = True
while calcular:
    escolha = input('Escolha entre somar (+), subtrair (-), multiplicar (*), dividir (/) ou sair (s): ')
    
    somar = escolha.startswith('+')
    subtrair = escolha.startswith('-')
    multiplicar = escolha.startswith('*')
    dividir = escolha.startswith('/')
    sair = escolha.startswith('s')
    
    if somar:
        valor1 = float(input('Digite o 1° valor da soma: '))
        valor2 = float(input('Digite o 2° valor da soma: '))
        soma = valor1 + valor2
        print(f'{valor1} + {valor2} = {soma}')
    elif sair:
        break
    else:
        print('Valor inválido.')