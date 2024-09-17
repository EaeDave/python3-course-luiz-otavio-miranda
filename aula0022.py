# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

login = input('Digite seu login: ')
password = input('Digite sua senha: ')
# print(entrada)

if (login == 'David' or login =='david') and password == 'programacao':  # Foi implementado o "or"
    print('Bem vindo ao sistema.')
else:
    print('Credenciais incorretas.')