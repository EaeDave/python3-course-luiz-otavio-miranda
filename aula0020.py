primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior do que o segundo.')
elif segundo_valor > primeiro_valor:
    print('O segundo valor é maior do que o primeiro valor.')
elif primeiro_valor == segundo_valor:
    print('Ambos os valores são iguais.')