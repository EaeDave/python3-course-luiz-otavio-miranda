# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

login = input('Digite seu login: ')
password = input('Digite sua senha: ')
# print(entrada)

if login == 'David' and password == 'programacao':
    print('Bem vindo ao sistema.')
else:
    print('Credenciais incorretas.')


print(True and True and 0)  # Retorna 0 por ser falsy.