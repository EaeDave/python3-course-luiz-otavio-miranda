"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'a'
# v3 = v2
# print(id(v1))
# print(id(v2))
# print(id(v3))

condicao = True  # variável declarada no escopo global do código
passou_no_if = None  # variável placeholder de valor
if condicao:
    passou_no_if = True  # nesse momento a variável recebeu um valor definitivo
    print('Faça algo')
# else:
#     passou_no_if = False
#     print('Não faça algo')


# exibe o valor da variável e verifica se o valor da mesma é None
print(passou_no_if, passou_no_if is None)

# exibe o valor da variável e verifica se o valor da mesma NÃO é None
print(passou_no_if, passou_no_if is not None)