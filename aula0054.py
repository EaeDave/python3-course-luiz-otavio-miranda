from os import system as console
"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
lista = []

OPCOES = ('1', '2', '3')

while True:
    print('##### Lista de Compras ####')
    opcao_escolhida = input('Escolha entre:\n\n[1] - Visualizar\n[2] - Inserir\n[3] - Apagar\nOpção:  ')
    
    if opcao_escolhida not in OPCOES:
        print(f'Você digitou "{opcao_escolhida}" - Opção inválida, tente novamente.')
        continue
    else:
        if opcao_escolhida == '1':
            if lista == []:
                console('cls')
                print('A lista está vazia = []')
            else:
                console('cls')
                print(lista)
        elif opcao_escolhida == '2':
            console('cls')
            produto = input('Digite o que deseja inserir na lista de compras: ')
            lista.append(produto)
            console('cls')
            print(f'"{produto}" inserido com sucesso!')
        elif opcao_escolhida == '3':
            console('cls')
            
            if lista == []:
                console('cls')
                print('A lista está vazia = []')
                continue
            else:
                for indice, produto in enumerate(lista):
                    print(f'[{indice}] {produto}')
                try:
                    indice = int(input('Digite o número referente ao item que deseja apagar: '))
                    console('cls')
                    try:
                        print(f'"{lista[indice]}" removido com sucesso!')
                        lista.pop(indice)
                    except IndexError:
                        print('Erro - o número digitado não referencia nenhum produto.')
                except ValueError:
                    console('cls')
                    print('Erro - Digite somente números.')


