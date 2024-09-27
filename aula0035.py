"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

# Sistema
while True:
    opcao = input('Digite a opção: [1] Escrever [2] Sair: ')

    if opcao == '1':
        escritura = input('Escreva: ')
        print(escritura)
    elif opcao == '2':
        break
    else:
        print('Valor digitado está incorreto.')


print('Acabou')